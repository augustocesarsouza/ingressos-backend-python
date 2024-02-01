import unittest
from unittest.mock import Mock

from src.api.Controllers.RegionController import RegionController
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.application.Services.Interfaces.IRegionService import IRegionService
from src.application.Services.ResponseWrapper import ResponseWrapper


class RegionControllerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_region_service = Mock(spec=IRegionService)

    def test_get_all_movie_by_region_id_without_error_status_code_200(self):
        self.mock_region_service.get_id_by_name_state.return_value = ResponseWrapper.ok(
            "ok")

        path_params = {'state': 'seila-state'}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        region_controller = RegionController(self.mock_region_service)

        result = region_controller.get_all_movie_by_region_id(http_request)
        self.assertEqual(result.status_code, 200)

    def test_get_all_movie_by_region_id_with_error_status_code_400(self):
        self.mock_region_service.get_id_by_name_state.return_value = ResponseWrapper.fail(
            "error get id name state")

        path_params = {'state': 'seila-state'}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        region_controller = RegionController(self.mock_region_service)

        result = region_controller.get_all_movie_by_region_id(http_request)
        self.assertEqual(result.status_code, 400)
