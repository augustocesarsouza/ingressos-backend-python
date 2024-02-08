import unittest
from unittest.mock import Mock

from src.api.Controllers.AdditionalFoodMovieController import AdditionalFoodMovieController
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.Validators.Interfaces.IAdditionalFoodMovieValidate import IAdditionalFoodMovieValidate
from src.application.Services.Interfaces.IAdditionalFoodMovieService import IAdditionalFoodMovieService
from src.application.Services.ResponseWrapper import ResponseWrapper


class Test_AdditionalFoodMovieController(unittest.TestCase):

    def setUp(self) -> None:
        self.mock_additional_food_movie_service = Mock(
            spec=IAdditionalFoodMovieService)
        self.mock_additional_food_movie_validate = Mock(
            spec=IAdditionalFoodMovieValidate)

    # test method "get_all_food_movie"
    def test_get_all_food_movie_withot_error_status_code_200(self):
        self.mock_additional_food_movie_service.get_all_food_movie.return_value = ResponseWrapper.ok(
            "get successfully")

        additional_food_movie_controller = AdditionalFoodMovieController(
            self.mock_additional_food_movie_service, self.mock_additional_food_movie_validate)

        path_params = {"movieId": "1087154a-3d32-45e2-a679-c30d753e1fa8"}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        result = additional_food_movie_controller.get_all_food_movie(
            http_request)
        self.assertEqual(result.status_code, 200)

    def test_get_all_food_movie_with_error_status_code_400(self):
        self.mock_additional_food_movie_service.get_all_food_movie.return_value = ResponseWrapper.fail(
            "error get all food movie")

        additional_food_movie_controller = AdditionalFoodMovieController(
            self.mock_additional_food_movie_service, self.mock_additional_food_movie_validate)

        path_params = {"movieId": "1087154a-3d32-45e2-a679-c30d753e1fa8"}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        result = additional_food_movie_controller.get_all_food_movie(
            http_request)
        self.assertEqual(result.status_code, 400)

    # test method "create"
    def test_create_withot_error_status_code_200(self):
        self.mock_additional_food_movie_validate.additional_food_create_validate.return_value = ResponseWrapper.ok(
            "validate body successfully")

        self.mock_additional_food_movie_service.create.return_value = ResponseWrapper.ok(
            "create successfully")

        additional_food_movie_controller = AdditionalFoodMovieController(
            self.mock_additional_food_movie_service, self.mock_additional_food_movie_validate)

        body = {"title": "COMBO BALDE CARAMELO MED", "price": "76.00", "fee": "7.59",
                "movieId": "d8e96e17-39b0-414a-a337-e920975db136", "base64Img": "base64Img1base64Img1"}

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        result = additional_food_movie_controller.create(
            http_request)
        self.assertEqual(result.status_code, 200)

    def test_create_with_error_status_code_422(self):
        self.mock_additional_food_movie_validate.additional_food_create_validate.return_value = ResponseWrapper.fail(
            "error when validate body")

        additional_food_movie_controller = AdditionalFoodMovieController(
            self.mock_additional_food_movie_service, self.mock_additional_food_movie_validate)

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=None, url=None, ipv4=None)

        result = additional_food_movie_controller.create(
            http_request)
        self.assertEqual(result.status_code, 422)

    def test_create_with_error_status_code_400(self):
        self.mock_additional_food_movie_validate.additional_food_create_validate.return_value = ResponseWrapper.ok(
            "validate body successfully")

        self.mock_additional_food_movie_service.create.return_value = ResponseWrapper.fail(
            "error create database")

        additional_food_movie_controller = AdditionalFoodMovieController(
            self.mock_additional_food_movie_service, self.mock_additional_food_movie_validate)

        body = {"title": "COMBO BALDE CARAMELO MED", "price": "76.00", "fee": "7.59",
                "movieId": "d8e96e17-39b0-414a-a337-e920975db136", "base64Img": "base64Img1base64Img1"}

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        result = additional_food_movie_controller.create(
            http_request)
        self.assertEqual(result.status_code, 400)
