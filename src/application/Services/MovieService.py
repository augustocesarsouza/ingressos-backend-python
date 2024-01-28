import uuid
from src.application.DTOs.MovieDTO import MovieDTO
from src.application.DTOs.RegionDTO import RegionDTO
from src.application.Services.Interfaces.IMovieService import IMovieService
from src.application.Services.Interfaces.IRegionService import IRegionService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IMovieRepository import IMovieRepository
from src.infradata.CloudinaryConfig.CloudinaryCreate import CloudinaryCreate
from src.infradata.Maps.MovieMap import MovieMap
from src.infradata.UtilityExternal.Interface.IClodinaryUti import IClodinaryUti


class MovieService(IMovieService):
    def __init__(self, movie_repository: IMovieRepository, region_service: IRegionService, clodinary_uti: IClodinaryUti) -> None:
        self.__movie_repository = movie_repository
        self.__region_service = region_service
        self.__clodinary_uti = clodinary_uti

    def get_all_movie_by_region_id(self, region: str) -> ResponseWrapper:
        id_region_result = self.__region_service.get_id_by_name_city(region)

        if not id_region_result.IsSuccess:
            return id_region_result

        region_obj: RegionDTO = id_region_result.Data

        movie_all_result = self.__movie_repository.get_all_movie_by_region_id(
            region_obj.Id)

        if movie_all_result.Data == None or len(movie_all_result.Data) <= 0:
            return ResponseWrapper.fail("we did not find movies")

        movie_all: list[MovieDTO] = movie_all_result.Data

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

        result_create_cloudinary = self.__clodinary_uti.create_img(
            movie_DTO.Base64Img, 625, 919)

        if not result_create_cloudinary.IsSuccess:
            return result_create_cloudinary

        result_img_background = self.__clodinary_uti.create_img(
            movie_DTO.Base64Img, 1440, 500)

        if not result_img_background.IsSuccess:
            return result_img_background

        create_img_base64: CloudinaryCreate = result_create_cloudinary.Data
        create_img_background: CloudinaryCreate = result_img_background.Data

        movie_DTO.add_imgUrl_PublicId_ImgUrlBackground_PublicIdImgBackgound(
            create_img_base64.img_url, create_img_base64.public_id, create_img_background.img_url, create_img_background.public_id)

        movie_map = MovieMap(Id=guid_str, Title=movie_DTO.Title, Description=movie_DTO.Description, Gender=movie_DTO.Gender, Duration=movie_DTO.Duration,
                             MovieRating=movie_DTO.MovieRating, ImgUrl=movie_DTO.ImgUrl, PublicId=movie_DTO.PublicId, ImgUrlBackground=movie_DTO.ImgUrlBackground,
                             PublicIdImgBackgound=movie_DTO.PublicIdImgBackgound, StatusMovie=movie_DTO.StatusMovie)

        print(movie_map.to_dict())

        result_create = self.__movie_repository.create(movie_map)

        if not result_create.IsSuccess:
            return result_create

        return result_create

    def delete_movie(self, id_movie: str) -> ResponseWrapper:
        pass

    def update_movie(self, movie_DTO: MovieDTO) -> ResponseWrapper:
        pass

    def update_movie_img_background(self, movie_DTO: MovieDTO) -> ResponseWrapper:
        pass
