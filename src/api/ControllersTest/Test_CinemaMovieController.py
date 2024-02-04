import unittest
from unittest.mock import Mock

from src.api.Controllers.CinemaMovieController import CinemaMovieController
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.Validators.Interfaces.ICinemaMovieValidate import ICinemaMovieValidate
from src.application.Services.Interfaces.ICinemaMovieService import ICinemaMovieService
from src.application.Services.ResponseWrapper import ResponseWrapper


class Test_CinemaMovieController(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_cinema_movie_service = Mock(ICinemaMovieService)
        self.mock_cinema_movie_validate = Mock(ICinemaMovieValidate)

    # method test "get_by_region_cinema_id_and_movie_id"
    def test_get_by_region_cinema_id_and_movie_id_without_error_status_code_200(self):
        self.mock_cinema_movie_service.get_by_region_cinema_id_and_movie_id.return_value = ResponseWrapper.ok(
            "Ok")

        cinema_movie_controller = CinemaMovieController(
            self.mock_cinema_movie_service, self.mock_cinema_movie_validate)

        path_params = {"region": "region1", "movieId": "movieId1"}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        result = cinema_movie_controller.get_by_region_cinema_id_and_movie_id(
            http_request)

        self.assertEqual(result.status_code, 200)

    def test_get_by_region_cinema_id_and_movie_id_with_error_status_code_400(self):
        self.mock_cinema_movie_service.get_by_region_cinema_id_and_movie_id.return_value = ResponseWrapper.fail(
            "error get")

        cinema_movie_controller = CinemaMovieController(
            self.mock_cinema_movie_service, self.mock_cinema_movie_validate)

        path_params = {"region": "region1", "movieId": "movieId1"}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        result = cinema_movie_controller.get_by_region_cinema_id_and_movie_id(
            http_request)

        self.assertEqual(result.status_code, 400)

    # method test "create"
    def test_create_without_error_status_code_200(self):
        self.mock_cinema_movie_validate.cinema_movie_create_validate.return_value = ResponseWrapper.ok(
            "ok body validated")

        self.mock_cinema_movie_service.create.return_value = ResponseWrapper.ok(
            "ok create successfylly")

        cinema_movie_controller = CinemaMovieController(
            self.mock_cinema_movie_service, self.mock_cinema_movie_validate)

        body = {"cinemaId": "f40ef4d7-87d8-4408-9ea7-a026e6a0909e",
                "movieId": "fd386e46-440d-48bd-8310-b0ca3c0107d2",
                "regionId": "b0284575-c91a-4fe1-b180-4f040634a367",
                "screeningSchedule": "8a77d1a2-5d83-42bc-9d2d-bc1147966ad0"}

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        result = cinema_movie_controller.create(
            http_request)

        self.assertEqual(result.status_code, 200)

    def test_create_with_error_status_code_422_error_validate_body(self):
        self.mock_cinema_movie_validate.cinema_movie_create_validate.return_value = ResponseWrapper.fail(
            "error validate body")

        cinema_movie_controller = CinemaMovieController(
            self.mock_cinema_movie_service, self.mock_cinema_movie_validate)

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=None, url=None, ipv4=None)

        result = cinema_movie_controller.create(
            http_request)

        self.assertEqual(result.status_code, 422)

    def test_create_with_error_status_code_400_error_create_cinema_movie(self):
        self.mock_cinema_movie_validate.cinema_movie_create_validate.return_value = ResponseWrapper.ok(
            "ok body validated")

        self.mock_cinema_movie_service.create.return_value = ResponseWrapper.fail(
            "error create cinema_movie")

        cinema_movie_controller = CinemaMovieController(
            self.mock_cinema_movie_service, self.mock_cinema_movie_validate)

        body = {"cinemaId": "f40ef4d7-87d8-4408-9ea7-a026e6a0909e",
                "movieId": "fd386e46-440d-48bd-8310-b0ca3c0107d2",
                "regionId": "b0284575-c91a-4fe1-b180-4f040634a367",
                "screeningSchedule": "8a77d1a2-5d83-42bc-9d2d-bc1147966ad0"}

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        result = cinema_movie_controller.create(
            http_request)

        self.assertEqual(result.status_code, 400)
