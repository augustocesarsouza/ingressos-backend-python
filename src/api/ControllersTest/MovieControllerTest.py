import unittest
from unittest.mock import Mock

from src.api.Controllers.MovieController import MovieController
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.Validators.Interfaces.IMovieValidate import IMovieValidate
from src.application.Services.Interfaces.IMovieService import IMovieService
from src.application.Services.ResponseWrapper import ResponseWrapper


class MovieControllerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_movie_service = Mock(spec=IMovieService)
        self.mock_movie_validate = Mock(spec=IMovieValidate)

    def test_get_all_movie_by_region_id_without_error(self):
        self.mock_movie_service.get_all_movie_by_region_id.return_value = ResponseWrapper.ok(
            "ok")

        path_params = {'region': 'seila'}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        movie_controller = MovieController(
            self.mock_movie_service, self.mock_movie_validate)

        result = movie_controller.get_all_movie_by_region_id(http_request)
        self.assertEqual(result.status_code, 200)

    def test_get_all_movie_by_region_id_with_error(self):
        self.mock_movie_service.get_all_movie_by_region_id.return_value = ResponseWrapper.fail(
            "error")

        path_params = {'region': 'seila'}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        movie_controller = MovieController(
            self.mock_movie_service, self.mock_movie_validate)

        result = movie_controller.get_all_movie_by_region_id(http_request)
        self.assertEqual(result.status_code, 400)

    def test_get_info_movies_by_id_without_error(self):
        self.mock_movie_service.get_info_movies_by_id.return_value = ResponseWrapper.ok(
            "ok")

        path_params = {'idGuid': 'seilaidseila'}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        movie_controller = MovieController(
            self.mock_movie_service, self.mock_movie_validate)

        result = movie_controller.get_info_movies_by_id(http_request)
        self.assertEqual(result.status_code, 200)

    def test_get_info_movies_by_id_with_error(self):
        self.mock_movie_service.get_info_movies_by_id.return_value = ResponseWrapper.fail(
            "error")

        path_params = {'idGuid': 'seilaidseila'}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        movie_controller = MovieController(
            self.mock_movie_service, self.mock_movie_validate)

        result = movie_controller.get_info_movies_by_id(http_request)
        self.assertEqual(result.status_code, 400)

    def test_get_status_movie_without_error(self):
        self.mock_movie_service.get_status_movie.return_value = ResponseWrapper.ok(
            "ok")

        path_params = {'statusMovie': 'statuseila'}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        movie_controller = MovieController(
            self.mock_movie_service, self.mock_movie_validate)

        result = movie_controller.get_status_movie(http_request)
        self.assertEqual(result.status_code, 200)

    def test_get_status_movie_with_error(self):
        self.mock_movie_service.get_status_movie.return_value = ResponseWrapper.fail(
            "error")

        path_params = {'statusMovie': 'statuseila'}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        movie_controller = MovieController(
            self.mock_movie_service, self.mock_movie_validate)

        result = movie_controller.get_status_movie(http_request)
        self.assertEqual(result.status_code, 400)

    def test_create_without_error(self):
        self.mock_movie_validate.movie_create_validate.return_value = ResponseWrapper.ok(
            "ok validate body movie")

        self.mock_movie_service.create.return_value = ResponseWrapper.ok(
            "ok create movie")

        body = {
            "title": "title1",
            "description": "description1",
            "gender": "gender1",
            "duration": "duration1",
            "statusMovie": "statusMovie1",
            "base64Img": "base64Img1",
            "movieRating": "movieRating1"
        }

        movie_controller = MovieController(
            self.mock_movie_service, self.mock_movie_validate)

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        result = movie_controller.create(http_request)
        self.assertEqual(result.status_code, 200)

    def test_create_with_error_validate_body_movie(self):
        self.mock_movie_validate.movie_create_validate.return_value = ResponseWrapper.fail(
            "error validating body movie")

        body = {
            "title": "title1",
            "description": "description1",
            "gender": "gender1",
            "duration": "duration1",
            "statusMovie": "statusMovie1",
            "base64Img": "base64Img1",
            "movieRating": "movieRating1"
        }

        movie_controller = MovieController(
            self.mock_movie_service, self.mock_movie_validate)

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        result = movie_controller.create(http_request)
        self.assertEqual(result.status_code, 422)

    def test_create_with_error_create_database(self):
        self.mock_movie_validate.movie_create_validate.return_value = ResponseWrapper.ok(
            "ok validate body movie")

        self.mock_movie_service.create.return_value = ResponseWrapper.fail(
            "error create movie")

        body = {
            "title": "title1",
            "description": "description1",
            "gender": "gender1",
            "duration": "duration1",
            "statusMovie": "statusMovie1",
            "base64Img": "base64Img1",
            "movieRating": "movieRating1"
        }

        movie_controller = MovieController(
            self.mock_movie_service, self.mock_movie_validate)

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        result = movie_controller.create(http_request)
        self.assertEqual(result.status_code, 400)

    def test_delete_movie_without_error(self):
        self.mock_movie_service.delete_movie.return_value = ResponseWrapper.ok(
            "ok get success")

        path_params = {'idMovie': 'idGuidseila'}

        movie_controller = MovieController(
            self.mock_movie_service, self.mock_movie_validate)

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        result = movie_controller.delete_movie(http_request)
        self.assertEqual(result.status_code, 200)

    def test_delete_movie_with_error(self):
        self.mock_movie_service.delete_movie.return_value = ResponseWrapper.fail(
            "error get delete movie")

        path_params = {'idMovie': 'idGuidseila'}

        movie_controller = MovieController(
            self.mock_movie_service, self.mock_movie_validate)

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        result = movie_controller.delete_movie(http_request)
        self.assertEqual(result.status_code, 400)

    def test_update_movie_without_error(self):
        self.mock_movie_validate.movie_update_validate.return_value = ResponseWrapper.ok(
            "ok validate body movie")

        self.mock_movie_service.update_movie.return_value = ResponseWrapper.ok(
            "ok update movie")

        body = {
            "id": "910d142a-9fcc-4ced-baac-5661c67d1bc2",
            "base64Img": "base64Img1"
        }

        movie_controller = MovieController(
            self.mock_movie_service, self.mock_movie_validate)

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        result = movie_controller.update_movie(http_request)
        self.assertEqual(result.status_code, 200)

    def test_update_movie_with_error_validate_body_update(self):
        self.mock_movie_validate.movie_update_validate.return_value = ResponseWrapper.fail(
            "error validate movie")

        movie_controller = MovieController(
            self.mock_movie_service, self.mock_movie_validate)

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=None, url=None, ipv4=None)

        result = movie_controller.update_movie(http_request)
        self.assertEqual(result.status_code, 422)

    def test_update_movie_with_error_update_movie(self):
        self.mock_movie_validate.movie_update_validate.return_value = ResponseWrapper.ok(
            "ok validate body movie")

        self.mock_movie_service.update_movie.return_value = ResponseWrapper.fail(
            "error update movie")

        body = {
            "id": "910d142a-9fcc-4ced-baac-5661c67d1bc2",
            "base64Img": "base64Img1"
        }

        movie_controller = MovieController(
            self.mock_movie_service, self.mock_movie_validate)

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        result = movie_controller.update_movie(http_request)
        self.assertEqual(result.status_code, 400)
