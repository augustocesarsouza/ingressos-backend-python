import unittest
from unittest.mock import Mock

from src.api.Controllers.MovieRegionTicketsPurchesedController import MovieRegionTicketsPurchesedController
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.Validators.Interfaces.IMovieRegionTicketsPurchesedValidate import IMovieRegionTicketsPurchesedValidate
from src.application.Services.Interfaces.IMovieRegionTicketsPurchesedService import IMovieRegionTicketsPurchesedService
from src.application.Services.ResponseWrapper import ResponseWrapper


class Test_MovieRegionTicketsPurchesedController(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_movie_region_tickets_purchesed_service = Mock(
            spec=IMovieRegionTicketsPurchesedService)
        self.movie_region_tickets_purchesed_validate = Mock(
            spec=IMovieRegionTicketsPurchesedValidate)

    # test method 'get_by_movie_id_and_cinema_id'
    def test_get_by_movie_id_and_cinema_id_without_error_status_code_200(self):
        self.mock_movie_region_tickets_purchesed_service.get_by_movie_id_and_cinema_id.return_value = ResponseWrapper.ok(
            "ok")

        path_params = {'movieId': '700b5f53-da49-419a-a514-59d4cc02e351',
                       'cinemaId': 'a07811b6-8492-474a-8f4e-e910832c0128'}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        movie_controller = MovieRegionTicketsPurchesedController(
            self.mock_movie_region_tickets_purchesed_service, self.movie_region_tickets_purchesed_validate)

        result = movie_controller.get_by_movie_id_and_cinema_id(http_request)
        self.assertEqual(result.status_code, 200)

    def test_get_by_movie_id_and_cinema_id_with_error_status_code_400(self):
        self.mock_movie_region_tickets_purchesed_service.get_by_movie_id_and_cinema_id.return_value = ResponseWrapper.fail(
            "fail get")

        path_params = {'movieId': '700b5f53-da49-419a-a514-59d4cc02e351',
                       'cinemaId': 'a07811b6-8492-474a-8f4e-e910832c0128'}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        movie_controller = MovieRegionTicketsPurchesedController(
            self.mock_movie_region_tickets_purchesed_service, self.movie_region_tickets_purchesed_validate)

        result = movie_controller.get_by_movie_id_and_cinema_id(http_request)
        self.assertEqual(result.status_code, 400)

    # test method 'create'
    def test_create_without_error_status_code_200(self):
        self.movie_region_tickets_purchesed_validate.movie_region_create_validate.return_value = ResponseWrapper.ok(
            "validated body successfully")

        self.mock_movie_region_tickets_purchesed_service.create.return_value = ResponseWrapper.ok(
            "created successfully")

        body = {'movieId': '700b5f53-da49-419a-a514-59d4cc02e351',
                'cinemaId': 'a07811b6-8492-474a-8f4e-e910832c0128', 'ticketsSeats': 'A1'}

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        movie_controller = MovieRegionTicketsPurchesedController(
            self.mock_movie_region_tickets_purchesed_service, self.movie_region_tickets_purchesed_validate)

        result = movie_controller.create(http_request)
        self.assertEqual(result.status_code, 200)

    def test_create_with_error_status_code_422(self):
        self.movie_region_tickets_purchesed_validate.movie_region_create_validate.return_value = ResponseWrapper.fail(
            "error validate body")

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=None, url=None, ipv4=None)

        movie_controller = MovieRegionTicketsPurchesedController(
            self.mock_movie_region_tickets_purchesed_service, self.movie_region_tickets_purchesed_validate)

        result = movie_controller.create(http_request)
        self.assertEqual(result.status_code, 422)

    def test_create_with_error_status_code_400(self):
        self.movie_region_tickets_purchesed_validate.movie_region_create_validate.return_value = ResponseWrapper.ok(
            "validated body successfully")

        self.mock_movie_region_tickets_purchesed_service.create.return_value = ResponseWrapper.fail(
            "error create")

        body = {'movieId': '700b5f53-da49-419a-a514-59d4cc02e351',
                'cinemaId': 'a07811b6-8492-474a-8f4e-e910832c0128', 'ticketsSeats': 'A1'}

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        movie_controller = MovieRegionTicketsPurchesedController(
            self.mock_movie_region_tickets_purchesed_service, self.movie_region_tickets_purchesed_validate)

        result = movie_controller.create(http_request)
        self.assertEqual(result.status_code, 400)

    # test method 'update'
    def test_update_without_error_status_code_200(self):
        self.movie_region_tickets_purchesed_validate.movie_region_update_validate.return_value = ResponseWrapper.ok(
            "validated body successfully")

        self.mock_movie_region_tickets_purchesed_service.update.return_value = ResponseWrapper.ok(
            "updated successfully")

        body = {'movieId': '700b5f53-da49-419a-a514-59d4cc02e351',
                'cinemaId': 'a07811b6-8492-474a-8f4e-e910832c0128', 'ticketsSeats': 'A1'}

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        movie_controller = MovieRegionTicketsPurchesedController(
            self.mock_movie_region_tickets_purchesed_service, self.movie_region_tickets_purchesed_validate)

        result = movie_controller.update(http_request)
        self.assertEqual(result.status_code, 200)

    def test_update_with_error_status_code_422(self):
        self.movie_region_tickets_purchesed_validate.movie_region_update_validate.return_value = ResponseWrapper.fail(
            "error validate body")

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=None, url=None, ipv4=None)

        movie_controller = MovieRegionTicketsPurchesedController(
            self.mock_movie_region_tickets_purchesed_service, self.movie_region_tickets_purchesed_validate)

        result = movie_controller.update(http_request)
        self.assertEqual(result.status_code, 422)

    def test_update_with_error_status_code_400(self):
        self.movie_region_tickets_purchesed_validate.movie_region_update_validate.return_value = ResponseWrapper.ok(
            "validated body successfully")

        self.mock_movie_region_tickets_purchesed_service.update.return_value = ResponseWrapper.fail(
            "error update")

        body = {'movieId': '700b5f53-da49-419a-a514-59d4cc02e351',
                'cinemaId': 'a07811b6-8492-474a-8f4e-e910832c0128', 'ticketsSeats': 'A1'}

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        movie_controller = MovieRegionTicketsPurchesedController(
            self.mock_movie_region_tickets_purchesed_service, self.movie_region_tickets_purchesed_validate)

        result = movie_controller.update(http_request)
        self.assertEqual(result.status_code, 400)
