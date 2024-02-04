import unittest
from unittest.mock import Mock

from src.api.Controllers.AdditionalInfoUserController import AdditionalInfoUserController
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.Validators.Interfaces.IAdditionalInfoUserValidate import IAdditionalInfoUserValidate
from src.application.Services.Interfaces.IAdditionalInfoUserService import IAdditionalInfoUserService
from src.application.Services.ResponseWrapper import ResponseWrapper


class Test_AdditionalInfoUserController(unittest.TestCase):

    def test_get_info_user_without_error_status_code_200(self):
        mock_additional_info_user_service = Mock(
            spec=IAdditionalInfoUserService)
        mock_additional_info_user_validate = Mock(
            spec=IAdditionalInfoUserValidate)

        mock_additional_info_user_service.get_info_user.return_value = ResponseWrapper.ok(
            "tudo certo")

        user_service = AdditionalInfoUserController(
            mock_additional_info_user_service, mock_additional_info_user_validate)

        path_params = {'idGuid': '19426g10-e431-4fc0-a828-e976c6d4yg4d'}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        response = user_service.get_info_user(http_request)
        self.assertEqual(response.status_code, 200)

    def test_get_info_user_error_status_400(self):
        mock_additional_info_user_service = Mock(
            spec=IAdditionalInfoUserService)
        mock_additional_info_user_validate = Mock(
            spec=IAdditionalInfoUserValidate)

        mock_additional_info_user_service.get_info_user.return_value = ResponseWrapper.fail(
            "error")

        user_service = AdditionalInfoUserController(
            mock_additional_info_user_service, mock_additional_info_user_validate)

        path_params = {'idGuid': '19426g10-e431-4fc0-a828-e976c6d4yg4d'}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        response = user_service.get_info_user(http_request)
        self.assertEqual(response.status_code, 400)

    def test_update_async_without_error_status_code_200(self):
        mock_additional_info_user_service = Mock(
            spec=IAdditionalInfoUserService)
        mock_additional_info_user_validate = Mock(
            spec=IAdditionalInfoUserValidate)

        mock_additional_info_user_validate.user_update_validate.return_value = ResponseWrapper.ok(
            "ok")

        mock_additional_info_user_service.update_async.return_value = ResponseWrapper.ok(
            "ok")

        user_service = AdditionalInfoUserController(
            mock_additional_info_user_service, mock_additional_info_user_validate)

        body = {
            "userId": "19426g10-e431-4fc0-a828-e976c6d4yg4d",
            "birthDateString": "05/10/1999",
            "gender": "",
            "phone": "67 981523696",
            "cep": "",
            "logradouro": "Rua Cajazeira",
            "numero": "2420",
            "complemento": "prox escola maria lucia passarelli",
            "referencia": "escolha passarelli",
            "bairro": "Jardim aero rancho",
            "estado": "MS",
            "cidade": "Campo grande"
        }

        path_params = {'password': 'password12345678'}

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=path_params, url=None, ipv4=None)

        response = user_service.update_async(http_request)
        self.assertEqual(response.status_code, 200)

    def test_update_async_with_error_status_code_422(self):
        mock_additional_info_user_service = Mock(
            spec=IAdditionalInfoUserService)
        mock_additional_info_user_validate = Mock(
            spec=IAdditionalInfoUserValidate)

        mock_additional_info_user_validate.user_update_validate.return_value = ResponseWrapper.fail(
            "error valid body")

        user_service = AdditionalInfoUserController(
            mock_additional_info_user_service, mock_additional_info_user_validate)

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=None, url=None, ipv4=None)

        response = user_service.update_async(http_request)
        self.assertEqual(response.status_code, 422)

    def test_update_async_with_error_status_code_400(self):
        mock_additional_info_user_service = Mock(
            spec=IAdditionalInfoUserService)
        mock_additional_info_user_validate = Mock(
            spec=IAdditionalInfoUserValidate)

        mock_additional_info_user_validate.user_update_validate.return_value = ResponseWrapper.ok(
            "ok")

        mock_additional_info_user_service.update_async.return_value = ResponseWrapper.fail(
            "error")

        user_service = AdditionalInfoUserController(
            mock_additional_info_user_service, mock_additional_info_user_validate)

        body = {
            "userId": "19426g10-e431-4fc0-a828-e976c6d4yg4d",
            "birthDateString": "05/10/1999",
            "gender": "",
            "phone": "67 981523696",
            "cep": "",
            "logradouro": "Rua Cajazeira",
            "numero": "2420",
            "complemento": "prox escola maria lucia passarelli",
            "referencia": "escolha passarelli",
            "bairro": "Jardim aero rancho",
            "estado": "MS",
            "cidade": "Campo grande"
        }

        path_params = {'password': 'password12345678'}

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=path_params, url=None, ipv4=None)

        response = user_service.update_async(http_request)
        self.assertEqual(response.status_code, 400)
