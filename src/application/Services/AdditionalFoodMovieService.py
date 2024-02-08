import uuid
from src.application.DTOs.AdditionalFoodMovieDTO import AdditionalFoodMovieDTO
from src.application.Services.Interfaces.IAdditionalFoodMovieService import IAdditionalFoodMovieService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IAdditionalFoodMovieRepository import IAdditionalFoodMovieRepository
from src.infradata.CloudinaryConfig.CloudinaryCreate import CloudinaryCreate
from src.infradata.Maps.AdditionalFoodMovieMap import AdditionalFoodMovieMap
from src.infradata.UtilityExternal.Interface.ICloudinaryUti import ICloudinaryUti


class AdditionalFoodMovieService(IAdditionalFoodMovieService):
    def __init__(self, additional_food_movie_repository: IAdditionalFoodMovieRepository, cloudinary_util: ICloudinaryUti) -> None:
        self.__additional_food_movie_repository = additional_food_movie_repository
        self.__cloudinary_util = cloudinary_util

    def get_all_food_movie(self, movie_id: str) -> ResponseWrapper:
        list_additional_food__movie = self.__additional_food_movie_repository.get_all_food_movie(
            movie_id)

        return list_additional_food__movie

    def create(self, additional_food_movie_dto: AdditionalFoodMovieDTO) -> ResponseWrapper:
        if additional_food_movie_dto == None:
            return ResponseWrapper.fail("error dto informed None")

        new_guid = uuid.uuid4()
        guid_str = str(new_guid)

        result_create_cloudinary = self.__cloudinary_util.create_img(
            additional_food_movie_dto.Base64Img, 210, 210)

        if not result_create_cloudinary.IsSuccess:
            return result_create_cloudinary

        create_img_base64: CloudinaryCreate = result_create_cloudinary.Data

        additional_food_movie_map = AdditionalFoodMovieMap(Id=guid_str, Title=additional_food_movie_dto.Title, Price=additional_food_movie_dto.Price,
                                                           Fee=additional_food_movie_dto.Fee, ImgUrl=create_img_base64.img_url, PublicId=create_img_base64.public_id, MovieId=additional_food_movie_dto.MovieId)

        result_create = self.__additional_food_movie_repository.create(
            additional_food_movie_map)

        return result_create

    def delete_additional_food_movie_by_movie_id(self, movie_id: str) -> ResponseWrapper:
        if len(movie_id) < 36:
            return ResponseWrapper.fail("movie_id less than 36")

        result_list_additional_food_movie = self.__additional_food_movie_repository.get_additional_food_movie_id_by_movie_id(
            movie_id)

        if not result_list_additional_food_movie.IsSuccess:
            return result_list_additional_food_movie

        list_addtional_food_movie: list[AdditionalFoodMovieDTO] = result_list_additional_food_movie.Data

        if len(list_addtional_food_movie) <= 0:
            return ResponseWrapper.ok("not exist registers")

        for el in list_addtional_food_movie:
            result_delete_additional_food_movie = self.__additional_food_movie_repository.delete(
                el.Id)

            if not result_delete_additional_food_movie.IsSuccess:
                return result_delete_additional_food_movie

            result_delete_img = self.__cloudinary_util.delete_img(el.PublicId)

            if not result_delete_img.IsSuccess:
                return result_delete_img

        return ResponseWrapper.ok("all delete successfully")
