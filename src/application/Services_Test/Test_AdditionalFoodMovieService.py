import unittest
from unittest.mock import Mock

from src.application.DTOs.AdditionalFoodMovieDTO import AdditionalFoodMovieDTO
from src.application.Services.AdditionalFoodMovieService import AdditionalFoodMovieService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IAdditionalFoodMovieRepository import IAdditionalFoodMovieRepository
from src.infradata.CloudinaryConfig.CloudinaryCreate import CloudinaryCreate
from src.infradata.UtilityExternal.Interface.ICloudinaryUti import ICloudinaryUti


class Test_AdditionalFoodMovieService(unittest.TestCase):

    def setUp(self) -> None:
        self.mock_additional_food_movie_repository = Mock(
            spec=IAdditionalFoodMovieRepository)
        self.mock_cloudinary_util = Mock(spec=ICloudinaryUti)

    # method test "get_all_food_movie"
    def test_get_all_food_movie_without_error(self):
        self.mock_additional_food_movie_repository.get_all_food_movie.return_value = ResponseWrapper.ok(
            "get successfully")

        movie_service = AdditionalFoodMovieService(
            self.mock_additional_food_movie_repository, self.mock_cloudinary_util)

        result = movie_service.get_all_food_movie(
            "6290a1e9-f3d2-4016-8082-ee4be3f840a9")
        self.assertEqual(result.IsSuccess, True)

    def test_get_all_food_movie_with_error(self):
        self.mock_additional_food_movie_repository.get_all_food_movie.return_value = ResponseWrapper.fail(
            "erro get_all_food_movie")

        movie_service = AdditionalFoodMovieService(
            self.mock_additional_food_movie_repository, self.mock_cloudinary_util)

        result = movie_service.get_all_food_movie(
            "6290a1e9-f3d2-4016-8082-ee4be3f840a9")
        self.assertEqual(result.IsSuccess, False)

    # method test "create"
    def test_create_without_error(self):
        create_img_base64 = CloudinaryCreate(
            "public_id1public_id1", "img_url1img_url1")

        self.mock_cloudinary_util.create_img.return_value = ResponseWrapper.ok(
            create_img_base64)

        self.mock_additional_food_movie_repository.create.return_value = ResponseWrapper.ok(
            "create successfully additional_food_movie")

        movie_service = AdditionalFoodMovieService(
            self.mock_additional_food_movie_repository, self.mock_cloudinary_util)

        additional_food_movie_dto = AdditionalFoodMovieDTO(id=None, title="COMBO BALDE CARAMELO MED", price="76.00",
                                                           fee="7.59", imgUrl=None, publicId=None, base64Img="base64Img1base64Img1", movieId="1240e5b4-bc4a-4e53-a02e-0a59033e9738", movie=None)

        result = movie_service.create(additional_food_movie_dto)
        self.assertEqual(result.IsSuccess, True)

    def test_create_with_error_dto_none(self):
        movie_service = AdditionalFoodMovieService(
            self.mock_additional_food_movie_repository, self.mock_cloudinary_util)

        result = movie_service.create(None)
        self.assertEqual(result.IsSuccess, False)
        self.assertEqual(result.Data["message"], "error dto informed None")

    def test_create_with_error_create_cloudinary(self):
        self.mock_cloudinary_util.create_img.return_value = ResponseWrapper.fail(
            "error create img")

        movie_service = AdditionalFoodMovieService(
            self.mock_additional_food_movie_repository, self.mock_cloudinary_util)

        additional_food_movie_dto = AdditionalFoodMovieDTO(id=None, title="COMBO BALDE CARAMELO MED", price="76.00",
                                                           fee="7.59", imgUrl=None, publicId=None, base64Img="base64Img1base64Img1", movieId="1240e5b4-bc4a-4e53-a02e-0a59033e9738", movie=None)

        result = movie_service.create(additional_food_movie_dto)
        self.assertEqual(result.IsSuccess, False)

    def test_create_with_error_create_database(self):
        create_img_base64 = CloudinaryCreate(
            "public_id1public_id1", "img_url1img_url1")

        self.mock_cloudinary_util.create_img.return_value = ResponseWrapper.ok(
            create_img_base64)

        self.mock_additional_food_movie_repository.create.return_value = ResponseWrapper.fail(
            "error create database")

        movie_service = AdditionalFoodMovieService(
            self.mock_additional_food_movie_repository, self.mock_cloudinary_util)

        additional_food_movie_dto = AdditionalFoodMovieDTO(id=None, title="COMBO BALDE CARAMELO MED", price="76.00",
                                                           fee="7.59", imgUrl=None, publicId=None, base64Img="base64Img1base64Img1", movieId="1240e5b4-bc4a-4e53-a02e-0a59033e9738", movie=None)

        result = movie_service.create(additional_food_movie_dto)
        self.assertEqual(result.IsSuccess, False)

    # method test "delete_additional_food_movie_by_movie_id"
    def test_delete_additional_food_movie_by_movie_id_without_error(self):
        list_addtional_food_movie = []

        additional_food_movie_dto = AdditionalFoodMovieDTO(id="777f584e-5f05-4766-aede-d55ca828a6d9", title=None, price=None,
                                                           fee=None, imgUrl=None, publicId="publicId1publicId1", base64Img=None, movieId=None, movie=None)

        list_addtional_food_movie.append(additional_food_movie_dto)

        self.mock_additional_food_movie_repository.get_additional_food_movie_id_by_movie_id.return_value = ResponseWrapper.ok(
            list_addtional_food_movie)

        self.mock_additional_food_movie_repository.delete.return_value = ResponseWrapper.ok(
            "delete obj successfully")

        self.mock_cloudinary_util.delete_img.return_value = ResponseWrapper.ok(
            "delete img successfully")

        movie_service = AdditionalFoodMovieService(
            self.mock_additional_food_movie_repository, self.mock_cloudinary_util)

        result = movie_service.delete_additional_food_movie_by_movie_id(
            "42c0da06-b1a9-4dec-a4d8-aa670f33f063")
        self.assertEqual(result.IsSuccess, True)

    def test_delete_additional_food_movie_by_movie_id_with_error_movieId_informed_less_than_36(self):
        movie_service = AdditionalFoodMovieService(
            self.mock_additional_food_movie_repository, self.mock_cloudinary_util)

        result = movie_service.delete_additional_food_movie_by_movie_id(
            "42c0da06-b1a9-4dec-a4d8-aa670f33f06")
        self.assertEqual(result.IsSuccess, False)

    def test_delete_additional_food_movie_by_movie_id_with_error_get_id(self):
        self.mock_additional_food_movie_repository.get_additional_food_movie_id_by_movie_id.return_value = ResponseWrapper.fail(
            "error get additional_food_movie_id")

        movie_service = AdditionalFoodMovieService(
            self.mock_additional_food_movie_repository, self.mock_cloudinary_util)

        result = movie_service.delete_additional_food_movie_by_movie_id(
            "42c0da06-b1a9-4dec-a4d8-aa670f33f063")
        self.assertEqual(result.IsSuccess, False)

    def test_delete_additional_food_movie_by_movie_id_with_error_list_empty(self):
        list_addtional_food_movie = []

        self.mock_additional_food_movie_repository.get_additional_food_movie_id_by_movie_id.return_value = ResponseWrapper.ok(
            list_addtional_food_movie)

        movie_service = AdditionalFoodMovieService(
            self.mock_additional_food_movie_repository, self.mock_cloudinary_util)

        result = movie_service.delete_additional_food_movie_by_movie_id(
            "42c0da06-b1a9-4dec-a4d8-aa670f33f063")
        self.assertEqual(result.IsSuccess, True)
        self.assertEqual(result.Data, "not exist registers")

    def test_delete_additional_food_movie_by_movie_id_with_error_delete_database(self):
        list_addtional_food_movie = []

        additional_food_movie_dto = AdditionalFoodMovieDTO(id="777f584e-5f05-4766-aede-d55ca828a6d9", title=None, price=None,
                                                           fee=None, imgUrl=None, publicId="publicId1publicId1", base64Img=None, movieId=None, movie=None)

        list_addtional_food_movie.append(additional_food_movie_dto)

        self.mock_additional_food_movie_repository.get_additional_food_movie_id_by_movie_id.return_value = ResponseWrapper.ok(
            list_addtional_food_movie)

        self.mock_additional_food_movie_repository.delete.return_value = ResponseWrapper.fail(
            "error delete database additional_food_movie")

        movie_service = AdditionalFoodMovieService(
            self.mock_additional_food_movie_repository, self.mock_cloudinary_util)

        result = movie_service.delete_additional_food_movie_by_movie_id(
            "42c0da06-b1a9-4dec-a4d8-aa670f33f063")
        self.assertEqual(result.IsSuccess, False)

    def test_delete_additional_food_movie_by_movie_id_with_error_delete_img_cloudinary(self):
        list_addtional_food_movie = []

        additional_food_movie_dto = AdditionalFoodMovieDTO(id="777f584e-5f05-4766-aede-d55ca828a6d9", title=None, price=None,
                                                           fee=None, imgUrl=None, publicId="publicId1publicId1", base64Img=None, movieId=None, movie=None)

        list_addtional_food_movie.append(additional_food_movie_dto)

        self.mock_additional_food_movie_repository.get_additional_food_movie_id_by_movie_id.return_value = ResponseWrapper.ok(
            list_addtional_food_movie)

        self.mock_additional_food_movie_repository.delete.return_value = ResponseWrapper.ok(
            "delete obj successfully")

        self.mock_cloudinary_util.delete_img.return_value = ResponseWrapper.fail(
            "error delete img cloudinary")

        movie_service = AdditionalFoodMovieService(
            self.mock_additional_food_movie_repository, self.mock_cloudinary_util)

        result = movie_service.delete_additional_food_movie_by_movie_id(
            "42c0da06-b1a9-4dec-a4d8-aa670f33f063")
        self.assertEqual(result.IsSuccess, False)
