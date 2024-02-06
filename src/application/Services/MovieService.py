import uuid
from src.application.DTOs.MovieDTO import MovieDTO
from src.application.DTOs.RegionDTO import RegionDTO
from src.application.Services.Interfaces.ICinemaMovieService import ICinemaMovieService
from src.application.Services.Interfaces.IFormOfPaymentService import IFormOfPaymentService
from src.application.Services.Interfaces.IMovieRegionTicketsPurchesedService import IMovieRegionTicketsPurchesedService
from src.application.Services.Interfaces.IMovieService import IMovieService
from src.application.Services.Interfaces.IMovieTheaterService import IMovieTheaterService
from src.application.Services.Interfaces.IRegionService import IRegionService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IMovieRepository import IMovieRepository
from src.infradata.CloudinaryConfig.CloudinaryCreate import CloudinaryCreate
from src.infradata.Maps.MovieMap import MovieMap
from src.infradata.UtilityExternal.Interface.ICloudinaryUti import ICloudinaryUti


class MovieService(IMovieService):
    def __init__(self, movie_repository: IMovieRepository, movie_theater_service: IMovieTheaterService, region_service: IRegionService, movie_region_tickets_purchesed_service: IMovieRegionTicketsPurchesedService, form_of_payment_service: IFormOfPaymentService, cinema_movie_service: ICinemaMovieService, cloudinary_util: ICloudinaryUti) -> None:
        self.__movie_repository = movie_repository
        self.__movie_theater_service = movie_theater_service
        self.__region_service = region_service
        self.__movie_region_tickets_purchesed_service = movie_region_tickets_purchesed_service
        self.__form_of_payment_service = form_of_payment_service
        self.__cinema_movie_service = cinema_movie_service
        self.__cloudinary_util = cloudinary_util

    def get_movie_by_id_check_exist(self, movie_id: str) -> ResponseWrapper:
        movie_result = self.__movie_repository.get_movie_by_id_check_exist(
            movie_id)

        if movie_result.Data == None:
            return ResponseWrapper.fail("not fould movie")

        if not movie_result.IsSuccess:
            return movie_result

        return movie_result

    def get_all_movie_by_region_id(self, state: str) -> ResponseWrapper:
        id_region_result = self.__region_service.get_id_by_name_state(state)

        if not id_region_result.IsSuccess:
            return id_region_result

        region_obj: RegionDTO = id_region_result.Data

        movie_all_result = self.__movie_repository.get_all_movie_by_region_id(
            region_obj.Id)

        if not movie_all_result.IsSuccess:
            return movie_all_result

        if movie_all_result.Data == None or len(movie_all_result.Data) <= 0:
            return ResponseWrapper.fail("we did not find movies")

        movie_all = movie_all_result.Data

        return ResponseWrapper.ok(movie_all)

    def get_info_movies_by_id(self, id: str) -> ResponseWrapper:
        movie_result = self.__movie_repository.get_info_movies_by_id(id)

        if movie_result.Data == None:
            return ResponseWrapper.fail("not fould movie")

        if not movie_result.IsSuccess:
            return movie_result

        return movie_result

    def get_status_movie(self, status_movie: str) -> ResponseWrapper:
        movie_result = self.__movie_repository.get_status_movie(status_movie)

        if movie_result.Data == None:
            return ResponseWrapper.fail("statusMovie not fould")

        if not movie_result.IsSuccess:
            return movie_result

        return movie_result

    def create(self, movie_DTO: MovieDTO) -> ResponseWrapper:
        if movie_DTO == None:
            return ResponseWrapper.fail("error obj null")

        new_guid = uuid.uuid4()
        guid_str = str(new_guid)

        result_create_cloudinary = self.__cloudinary_util.create_img(
            movie_DTO.Base64Img, 625, 919)

        if not result_create_cloudinary.IsSuccess:
            return result_create_cloudinary

        result_img_background = self.__cloudinary_util.create_img(
            movie_DTO.Base64Img, 1440, 500)

        if not result_img_background.IsSuccess:
            return result_img_background

        create_img_base64: CloudinaryCreate = result_create_cloudinary.Data
        create_img_background: CloudinaryCreate = result_img_background.Data

        movie_map = MovieMap(Id=guid_str, Title=movie_DTO.Title, Description=movie_DTO.Description, Gender=movie_DTO.Gender, Duration=movie_DTO.Duration,
                             MovieRating=movie_DTO.MovieRating, ImgUrl=create_img_base64.img_url, PublicId=create_img_base64.public_id, ImgUrlBackground=create_img_background.img_url,
                             PublicIdImgBackgound=create_img_background.public_id, StatusMovie=movie_DTO.StatusMovie)

        result_create = self.__movie_repository.create(movie_map)

        return result_create

    def delete_movie(self, id_movie: str) -> ResponseWrapper:
        movie_get_result = self.__movie_repository.get_by_id(
            id_movie)

        if movie_get_result.Data == None:
            return ResponseWrapper.fail("not fould movie")

        if not movie_get_result.IsSuccess:
            return movie_get_result

        delete_movie_theater_result = self.__movie_theater_service.delete(
            id_movie)

        if not delete_movie_theater_result.IsSuccess:
            return delete_movie_theater_result

        delete_movie_region_tickets_purchesed = self.__movie_region_tickets_purchesed_service.delete(
            id_movie)

        if not delete_movie_region_tickets_purchesed.IsSuccess:
            return delete_movie_region_tickets_purchesed

        delete_relation_between_form_payment_and_movie = self.__form_of_payment_service.delete(
            id_movie)

        if not delete_relation_between_form_payment_and_movie.IsSuccess:
            return delete_relation_between_form_payment_and_movie

        delete_relation_between_cinema_movie_and_movie = self.__cinema_movie_service.delete(
            id_movie)

        if not delete_relation_between_cinema_movie_and_movie.IsSuccess:
            return delete_relation_between_cinema_movie_and_movie

        movie_delete_result = self.__movie_repository.delete(id_movie)

        if not movie_delete_result.IsSuccess:
            return movie_delete_result

        movie_dto_delete: MovieDTO = movie_delete_result.Data

        # mesmo que der algum erro ao deletar no cloudinary ele já deletou no banco de dados o mivie
        result_delete_img_main = self.__cloudinary_util.delete_img(
            movie_dto_delete["publicId"])

        if not result_delete_img_main.IsSuccess:
            return result_delete_img_main

        result_delete_img_background = self.__cloudinary_util.delete_img(
            movie_dto_delete["publicIdImgBackgound"])

        if not result_delete_img_background.IsSuccess:
            return result_delete_img_background

        return movie_delete_result

    def update_movie(self, movie_DTO: MovieDTO) -> ResponseWrapper:
        movie_update = self.__movie_repository.get_by_id_only_publicId_PublicIdImgBackgound(
            movie_DTO.Id)

        if not movie_update.IsSuccess:
            return movie_update

        if movie_update.Data == None:
            return ResponseWrapper.fail("not fould movie")

        movie_update_obj: MovieDTO = movie_update.Data
        result_delete_img_main = self.__cloudinary_util.delete_img(
            movie_update_obj.PublicId)

        if not result_delete_img_main.IsSuccess:
            return result_delete_img_main

        result_delete_img_background = self.__cloudinary_util.delete_img(
            movie_update_obj.PublicIdImgBackgound)

        if not result_delete_img_background.IsSuccess:
            return result_delete_img_background

        result_create_cloudinary = self.__cloudinary_util.create_img(
            movie_DTO.Base64Img, 625, 919)

        if not result_create_cloudinary.IsSuccess:
            return result_create_cloudinary

        result_img_background = self.__cloudinary_util.create_img(
            movie_DTO.Base64Img, 1440, 500)

        if not result_img_background.IsSuccess:
            return result_img_background

        create_img_base64: CloudinaryCreate = result_create_cloudinary.Data
        create_img_background: CloudinaryCreate = result_img_background.Data

        movie_DTO.add_imgUrl_PublicId_ImgUrlBackground_PublicIdImgBackgound(
            create_img_base64.img_url, create_img_base64.public_id, create_img_background.img_url, create_img_background.public_id)

        result_update_movie = self.__movie_repository.update_movie(movie_DTO)

        if not result_update_movie.IsSuccess:
            return result_update_movie

        return result_update_movie
