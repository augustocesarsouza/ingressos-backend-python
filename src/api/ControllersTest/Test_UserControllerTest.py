import unittest
from unittest.mock import Mock

from src.api.Controllers.UserController import UserController
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.Validators.Interfaces.IUserCreateValidate import IUserCreateValidate
from src.application.Services.Interfaces.IUserAuthenticationService import IUserAuthenticationService
from src.application.Services.Interfaces.IUserConfirmationService import IUserConfirmationService
from src.application.Services.Interfaces.IUserManagementService import IUserManagementService
from src.application.Services.ResponseWrapper import ResponseWrapper


class Test_UserControllerTest(unittest.TestCase):

    def test_create_async_without_error(self):
        mock_user_menagement_service = Mock(spec=IUserManagementService)
        mock_user_authentication_service = Mock(
            spec=IUserAuthenticationService)
        mock_user_confirmation_service = Mock(spec=IUserConfirmationService)
        mock_user_create_validate = Mock(spec=IUserCreateValidate)

        mock_user_create_validate.user_create_validate.return_value = ResponseWrapper.ok(
            "tudo certo")

        mock_user_menagement_service.create_async.return_value = ResponseWrapper.ok(
            "tudo certo")

        user_service = UserController(
            mock_user_menagement_service, mock_user_authentication_service, mock_user_confirmation_service, mock_user_create_validate)

        body = {
            "name": "lucas daniel",
            "email": "lucasdaniel@gmail.com",
            "cpf": "232323232323",
            "password": "sdvsdvdsvsdasdcasca",
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

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        response = user_service.create_async(http_request)
        self.assertEqual(response.status_code, 200)

    def test_create_async_with_error_valid_body(self):
        mock_user_menagement_service = Mock(spec=IUserManagementService)
        mock_user_authentication_service = Mock(
            spec=IUserAuthenticationService)
        mock_user_confirmation_service = Mock(spec=IUserConfirmationService)
        mock_user_create_validate = Mock(spec=IUserCreateValidate)

        mock_user_create_validate.user_create_validate.return_value = ResponseWrapper.fail(
            "error validar BODY")

        user_service = UserController(
            mock_user_menagement_service, mock_user_authentication_service, mock_user_confirmation_service, mock_user_create_validate)

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=None, url=None, ipv4=None)

        response = user_service.create_async(http_request)
        self.assertEqual(response.status_code, 422)

    def test_create_async_without_error(self):
        mock_user_menagement_service = Mock(spec=IUserManagementService)
        mock_user_authentication_service = Mock(
            spec=IUserAuthenticationService)
        mock_user_confirmation_service = Mock(spec=IUserConfirmationService)
        mock_user_create_validate = Mock(spec=IUserCreateValidate)

        mock_user_create_validate.user_create_validate.return_value = ResponseWrapper.ok(
            "tudo certo")

        mock_user_menagement_service.create_async.return_value = ResponseWrapper.fail(
            "error criar user")

        user_service = UserController(
            mock_user_menagement_service, mock_user_authentication_service, mock_user_confirmation_service, mock_user_create_validate)

        body = {
            "name": "lucas daniel",
            "email": "lucasdaniel@gmail.com",
            "cpf": "232323232323",
            "password": "sdvsdvdsvsdasdcasca",
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

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        response = user_service.create_async(http_request)
        self.assertEqual(response.status_code, 400)

    def test_login_user_without_error(self):
        mock_user_menagement_service = Mock(spec=IUserManagementService)
        mock_user_authentication_service = Mock(
            spec=IUserAuthenticationService)
        mock_user_confirmation_service = Mock(spec=IUserConfirmationService)
        mock_user_create_validate = Mock(spec=IUserCreateValidate)

        mock_user_authentication_service.login.return_value = ResponseWrapper.ok(
            "tudo certo")

        user_service = UserController(
            mock_user_menagement_service, mock_user_authentication_service, mock_user_confirmation_service, mock_user_create_validate)

        path_params = {'cpfOrEmail': 'augusto@gmail.com',
                       'password': 'login123'}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        response = user_service.login_user(http_request)
        self.assertEqual(response.status_code, 200)

    def test_login_user_with_error(self):
        mock_user_menagement_service = Mock(spec=IUserManagementService)
        mock_user_authentication_service = Mock(
            spec=IUserAuthenticationService)
        mock_user_confirmation_service = Mock(spec=IUserConfirmationService)
        mock_user_create_validate = Mock(spec=IUserCreateValidate)

        mock_user_authentication_service.login.return_value = ResponseWrapper.fail(
            "falha ao logar")

        user_service = UserController(
            mock_user_menagement_service, mock_user_authentication_service, mock_user_confirmation_service, mock_user_create_validate)

        path_params = {'cpfOrEmail': 'augusto@gmail.com',
                       'password': 'login123'}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        response = user_service.login_user(http_request)
        self.assertEqual(response.status_code, 400)

    def test_verfic_token_without_error(self):
        mock_user_menagement_service = Mock(spec=IUserManagementService)
        mock_user_authentication_service = Mock(
            spec=IUserAuthenticationService)
        mock_user_confirmation_service = Mock(spec=IUserConfirmationService)
        mock_user_create_validate = Mock(spec=IUserCreateValidate)

        mock_user_authentication_service.verfic_token.return_value = ResponseWrapper.ok(
            "tudo certo")

        user_service = UserController(
            mock_user_menagement_service, mock_user_authentication_service, mock_user_confirmation_service, mock_user_create_validate)

        path_params = {'code': '123456',
                       'guidId': '19426g10-e431-4fc0-a828-e976c6d4yg4d'}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        response = user_service.verfic_token(http_request)
        self.assertEqual(response.status_code, 200)

    def test_verfic_token_with_error(self):
        mock_user_menagement_service = Mock(spec=IUserManagementService)
        mock_user_authentication_service = Mock(
            spec=IUserAuthenticationService)
        mock_user_confirmation_service = Mock(spec=IUserConfirmationService)
        mock_user_create_validate = Mock(spec=IUserCreateValidate)

        mock_user_authentication_service.verfic_token.return_value = ResponseWrapper.fail(
            "falha ao verifcar token")

        user_service = UserController(
            mock_user_menagement_service, mock_user_authentication_service, mock_user_confirmation_service, mock_user_create_validate)

        path_params = {'code': '123456',
                       'guidId': '19426g10-e431-4fc0-a828-e976c6d4yg4d'}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        response = user_service.verfic_token(http_request)
        self.assertEqual(response.status_code, 400)

    def test_get_confirm_token_without_error(self):
        mock_user_menagement_service = Mock(spec=IUserManagementService)
        mock_user_authentication_service = Mock(
            spec=IUserAuthenticationService)
        mock_user_confirmation_service = Mock(spec=IUserConfirmationService)
        mock_user_create_validate = Mock(spec=IUserCreateValidate)

        mock_user_confirmation_service.get_confirm_token.return_value = ResponseWrapper.ok(
            "tudo certo")

        user_service = UserController(
            mock_user_menagement_service, mock_user_authentication_service, mock_user_confirmation_service, mock_user_create_validate)

        path_params = {'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDYxMjkyNzgsImlkIjoiMzY0ODZhNzAtZTQzMS00ZmMwLWE4MjgtZTk3NmM2ZDdiYzlmIn0.E81m1yZDSiELLwU2qcdyVXh7WCnKTKUQo9Kz7UxucH4'}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        response = user_service.get_confirm_token(http_request)
        self.assertEqual(response.status_code, 200)

    def test_get_confirm_token_with_error(self):
        mock_user_menagement_service = Mock(spec=IUserManagementService)
        mock_user_authentication_service = Mock(
            spec=IUserAuthenticationService)
        mock_user_confirmation_service = Mock(spec=IUserConfirmationService)
        mock_user_create_validate = Mock(spec=IUserCreateValidate)

        mock_user_confirmation_service.get_confirm_token.return_value = ResponseWrapper.fail(
            "falha ao cofirmar token")

        user_service = UserController(
            mock_user_menagement_service, mock_user_authentication_service, mock_user_confirmation_service, mock_user_create_validate)

        path_params = {'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDYxMjkyNzgsImlkIjoiMzY0ODZhNzAtZTQzMS00ZmMwLWE4MjgtZTk3NmM2ZDdiYzlmIn0.E81m1yZDSiELLwU2qcdyVXh7WCnKTKUQo9Kz7UxucH4'}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        response = user_service.get_confirm_token(http_request)
        self.assertEqual(response.status_code, 400)
