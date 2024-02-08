import unittest
from unittest.mock import Mock

from src.api.Controllers.FormOfPaymentController import FormOfPaymentController
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.Validators.Interfaces.IFormOfPaymentValidate import IFormOfPaymentValidate
from src.application.Services.Interfaces.IFormOfPaymentService import IFormOfPaymentService
from src.application.Services.ResponseWrapper import ResponseWrapper


class Test_FormOfPaymentController(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_form_of_payment_service = Mock(spec=IFormOfPaymentService)
        self.mock_form_of_payment_validate = Mock(spec=IFormOfPaymentValidate)

    # test method "get_movie_Id_info"
    def test_get_movie_Id_info_withot_error_status_code_200(self):
        self.mock_form_of_payment_service.get_movie_Id_info.return_value = ResponseWrapper.ok(
            "get successfully")

        form_of_payment_controller = FormOfPaymentController(
            self.mock_form_of_payment_service, self.mock_form_of_payment_validate)

        path_params = {"movieid": "1087154a-3d32-45e2-a679-c30d753e1fa8"}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        result = form_of_payment_controller.get_movie_Id_info(http_request)
        self.assertEqual(result.status_code, 200)

    def test_get_movie_Id_info_with_error_status_code_400(self):
        self.mock_form_of_payment_service.get_movie_Id_info.return_value = ResponseWrapper.fail(
            "error get")

        form_of_payment_controller = FormOfPaymentController(
            self.mock_form_of_payment_service, self.mock_form_of_payment_validate)

        path_params = {"movieid": "1087154a-3d32-45e2-a679-c30d753e1fa8"}

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=path_params, url=None, ipv4=None)

        result = form_of_payment_controller.get_movie_Id_info(http_request)
        self.assertEqual(result.status_code, 400)

    # test method "create"
    def test_create_withot_error_status_code_200(self):
        self.mock_form_of_payment_validate.form_of_payment_create_validate.return_value = ResponseWrapper.ok(
            "validate body successfully")

        form_of_payment_controller = FormOfPaymentController(
            self.mock_form_of_payment_service, self.mock_form_of_payment_validate)

        body = {"formName": "Voucher Eletrônico",
                "price": "0,00",
                "movieId": "a8e76a89-64aa-40ee-89ad-72f4869a4702"}

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        result = form_of_payment_controller.create(http_request)
        self.assertEqual(result.status_code, 200)

    def test_create_with_error_status_code_422_validate_body(self):
        self.mock_form_of_payment_validate.form_of_payment_create_validate.return_value = ResponseWrapper.fail(
            "error validate body")

        form_of_payment_controller = FormOfPaymentController(
            self.mock_form_of_payment_service, self.mock_form_of_payment_validate)

        http_request = HttpRequest(
            headers=None, body=None, query_params=None, path_params=None, url=None, ipv4=None)

        result = form_of_payment_controller.create(http_request)
        self.assertEqual(result.status_code, 422)

    def test_create_with_error_status_code_400(self):
        self.mock_form_of_payment_validate.form_of_payment_create_validate.return_value = ResponseWrapper.ok(
            "validate body successfully")

        self.mock_form_of_payment_service.create.return_value = ResponseWrapper.fail(
            "error when create")

        form_of_payment_controller = FormOfPaymentController(
            self.mock_form_of_payment_service, self.mock_form_of_payment_validate)

        body = {"formName": "Voucher Eletrônico",
                "price": "0,00",
                "movieId": "a8e76a89-64aa-40ee-89ad-72f4869a4702"}

        http_request = HttpRequest(
            headers=None, body=body, query_params=None, path_params=None, url=None, ipv4=None)

        result = form_of_payment_controller.create(http_request)
        self.assertEqual(result.status_code, 400)
