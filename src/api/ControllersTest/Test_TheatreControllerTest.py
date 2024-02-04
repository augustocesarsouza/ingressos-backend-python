import unittest
from unittest.mock import Mock

from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.Validators.Interfaces.ITheatreValidate import ITheatreValidate
from src.application.Services.Interfaces.ITheatreService import ITheatreService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.api.Controllers.TheatreController import TheatreController


class Test_TheatreControllerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_theatre_service = Mock(spec=ITheatreService)
        self.mock_theatre_validate = Mock(spec=ITheatreValidate)

    # test method "get_all_theatre_by_state_name"
    def test_get_all_theatre_by_state_name_without_error_status_code_200(self):
        self.mock_theatre_service.get_all_theatre_by_state_name.return_value = ResponseWrapper.ok(
            "ok")

        path_params = {'state': 'seila-state'}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        region_controller = TheatreController(
            self.mock_theatre_service, self.mock_theatre_validate)

        result = region_controller.get_all_theatre_by_state_name(http_request)
        self.assertEqual(result.status_code, 200)

    def test_get_all_theatre_by_state_name_with_error_status_code_400(self):
        self.mock_theatre_service.get_all_theatre_by_state_name.return_value = ResponseWrapper.fail(
            "fail")

        path_params = {'state': 'seila-state'}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        region_controller = TheatreController(
            self.mock_theatre_service, self.mock_theatre_validate)

        result = region_controller.get_all_theatre_by_state_name(http_request)
        self.assertEqual(result.status_code, 400)

    # test method "create"
    def test_create_without_error_status_code_200(self):
        self.mock_theatre_validate.theatre_create_validate.return_value = ResponseWrapper.ok(
            "ok, body valid")

        self.mock_theatre_service.create.return_value = ResponseWrapper.ok(
            "ok")

        body = {'title': 'title1',
                'description': 'description1',
                'location': 'location1',
                'typeOfAttraction': 'typeOfAttraction1',
                'category': 'category1',
                'base64Img': 'base64Img1',
                'dataString': 'dataString1'}

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        region_controller = TheatreController(
            self.mock_theatre_service, self.mock_theatre_validate)

        result = region_controller.create(http_request)
        self.assertEqual(result.status_code, 200)

    def test_create_with_error_status_code_422_validate_body(self):
        self.mock_theatre_validate.theatre_create_validate.return_value = ResponseWrapper.fail(
            "fail validate body")

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=None, url=None, ipv4=None)

        region_controller = TheatreController(
            self.mock_theatre_service, self.mock_theatre_validate)

        result = region_controller.create(http_request)
        self.assertEqual(result.status_code, 422)

    def test_create_with_error_status_code_400(self):
        self.mock_theatre_validate.theatre_create_validate.return_value = ResponseWrapper.ok(
            "ok, body valid")

        self.mock_theatre_service.create.return_value = ResponseWrapper.fail(
            "error create theatre")

        body = {'title': 'title1',
                'description': 'description1',
                'location': 'location1',
                'typeOfAttraction': 'typeOfAttraction1',
                'category': 'category1',
                'base64Img': 'base64Img1',
                'dataString': 'dataString1'}

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        region_controller = TheatreController(
            self.mock_theatre_service, self.mock_theatre_validate)

        result = region_controller.create(http_request)
        self.assertEqual(result.status_code, 400)

    # test method "delete"
    def test_delete_without_error_status_code_200(self):
        self.mock_theatre_service.delete.return_value = ResponseWrapper.ok(
            "ok, deleted")

        path_params = {"idTheatre": "test"}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        region_controller = TheatreController(
            self.mock_theatre_service, self.mock_theatre_validate)

        result = region_controller.delete(http_request)
        self.assertEqual(result.status_code, 200)

    def test_delete_with_error_status_code_400(self):
        self.mock_theatre_service.delete.return_value = ResponseWrapper.fail(
            "failed to delete")

        path_params = {"idTheatre": "test"}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        region_controller = TheatreController(
            self.mock_theatre_service, self.mock_theatre_validate)

        result = region_controller.delete(http_request)
        self.assertEqual(result.status_code, 400)

    # test method "update"
    def test_update_without_error_status_code_200(self):
        self.mock_theatre_validate.theatre_update_img_validate.return_value = ResponseWrapper.ok(
            "ok, body valid")

        self.mock_theatre_service.update_theatre_img.return_value = ResponseWrapper.ok(
            "updated successfully")

        body = {
            "id": "50334cf0-a2bf-411a-9055-af4b786d109e",
            "base64Img": "base64Img1"
        }

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        region_controller = TheatreController(
            self.mock_theatre_service, self.mock_theatre_validate)

        result = region_controller.update(http_request)
        self.assertEqual(result.status_code, 200)

    def test_update_with_error_status_code_422_validate_body(self):
        self.mock_theatre_validate.theatre_update_img_validate.return_value = ResponseWrapper.fail(
            "error validate body")

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=None, url=None, ipv4=None)

        region_controller = TheatreController(
            self.mock_theatre_service, self.mock_theatre_validate)

        result = region_controller.update(http_request)
        self.assertEqual(result.status_code, 422)

    def test_update_with_error_status_code_400(self):
        self.mock_theatre_validate.theatre_update_img_validate.return_value = ResponseWrapper.ok(
            "ok, body valid")

        self.mock_theatre_service.update_theatre_img.return_value = ResponseWrapper.fail(
            "error updated theatre")

        body = {
            "id": "50334cf0-a2bf-411a-9055-af4b786d109e",
            "base64Img": "base64Img1"
        }

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        region_controller = TheatreController(
            self.mock_theatre_service, self.mock_theatre_validate)

        result = region_controller.update(http_request)
        self.assertEqual(result.status_code, 400)
