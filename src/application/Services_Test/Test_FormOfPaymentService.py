import unittest
from unittest.mock import Mock
from src.application.DTOs.FormOfPaymentDTO import FormOfPaymentDTO

from src.application.Services.FormOfPaymentService import FormOfPaymentService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IFormOfPaymentRepository import IFormOfPaymentRepository


class Test_FormOfPaymentService(unittest.TestCase):

    def setUp(self) -> None:
        self.mock_form_of_payment_repository = Mock(
            spec=IFormOfPaymentRepository)

    # method test "get_movie_Id_info"
    def test_get_movie_Id_info_without_error(self):
        self.mock_form_of_payment_repository.get_movie_Id_info.return_value = ResponseWrapper.ok(
            "get successfully")

        form_of_payment_service = FormOfPaymentService(
            self.mock_form_of_payment_repository)

        result = form_of_payment_service.get_movie_Id_info(
            "60680338-0cfb-4501-82ea-4915dae29198")

        self.assertEqual(result.IsSuccess, True)

    def test_get_movie_Id_info_with_error(self):
        self.mock_form_of_payment_repository.get_movie_Id_info.return_value = ResponseWrapper.fail(
            "error get get_movie_Id_info")

        form_of_payment_service = FormOfPaymentService(
            self.mock_form_of_payment_repository)

        result = form_of_payment_service.get_movie_Id_info(
            "60680338-0cfb-4501-82ea-4915dae29198")

        self.assertEqual(result.IsSuccess, False)

    # method test "create"
    def test_create_without_error(self):
        self.mock_form_of_payment_repository.create.return_value = ResponseWrapper.ok(
            "create successfully")

        form_of_payment_service = FormOfPaymentService(
            self.mock_form_of_payment_repository)

        form_of_payment_dto = FormOfPaymentDTO(
            id=None, formName="Voucher Eletrônico", price="0,00", movieId="1bceb9a1-5765-4f15-9896-b0c8b3a016c1")

        result = form_of_payment_service.create(form_of_payment_dto)

        self.assertEqual(result.IsSuccess, True)

    def test_create_with_error_DTO_None(self):
        form_of_payment_service = FormOfPaymentService(
            self.mock_form_of_payment_repository)

        result = form_of_payment_service.create(None)

        self.assertEqual(result.IsSuccess, False)
        self.assertEqual(result.Data["message"], "dto informed is null")

    def test_create_with_error(self):
        self.mock_form_of_payment_repository.create.return_value = ResponseWrapper.fail(
            "error create")

        form_of_payment_service = FormOfPaymentService(
            self.mock_form_of_payment_repository)

        form_of_payment_dto = FormOfPaymentDTO(
            id=None, formName="Voucher Eletrônico", price="0,00", movieId="1bceb9a1-5765-4f15-9896-b0c8b3a016c1")

        result = form_of_payment_service.create(form_of_payment_dto)

        self.assertEqual(result.IsSuccess, False)

    # method test "delete"
    def test_delete_without_error(self):
        array = []

        form_of_payment_dto1 = FormOfPaymentDTO(
            id="ef037304-3fe5-41e3-b088-c00aad03c7bd", formName=None, price=None, movieId=None).to_dict()

        form_of_payment_dto2 = FormOfPaymentDTO(
            id="bbee5ce5-390b-43e5-ace6-1ae716c57592", formName=None, price=None, movieId=None).to_dict()

        array.append(form_of_payment_dto1)
        array.append(form_of_payment_dto2)

        self.mock_form_of_payment_repository.get_all_form_of_payment_id_by_movie_id.return_value = ResponseWrapper.ok(
            array)

        self.mock_form_of_payment_repository.delete.side_effect = [
            ResponseWrapper.ok("Delete successfully"),
            ResponseWrapper.ok("Delete successfully")
        ]

        form_of_payment_service = FormOfPaymentService(
            self.mock_form_of_payment_repository)

        result = form_of_payment_service.delete(
            "1bceb9a1-5765-4f15-9896-b0c8b3a016c1")

        self.assertEqual(result.IsSuccess, True)

    def test_delete_with_error_movie_id_less_than36(self):
        form_of_payment_service = FormOfPaymentService(
            self.mock_form_of_payment_repository)

        result = form_of_payment_service.delete(
            "1bceb9a1-5765-4f15-9896-b0c8b3a016c")

        self.assertEqual(result.IsSuccess, False)
        self.assertEqual(
            result.Data["message"], "error movie_id provided must be greater than or equal to 36")

    def test_delete_with_error_get_all_form_payment_id(self):
        self.mock_form_of_payment_repository.get_all_form_of_payment_id_by_movie_id.return_value = ResponseWrapper.fail(
            "error get all")

        form_of_payment_service = FormOfPaymentService(
            self.mock_form_of_payment_repository)

        result = form_of_payment_service.delete(
            "1bceb9a1-5765-4f15-9896-b0c8b3a016c1")

        self.assertEqual(result.IsSuccess, False)

    def test_delete_with_error_list_empty(self):
        array = []

        self.mock_form_of_payment_repository.get_all_form_of_payment_id_by_movie_id.return_value = ResponseWrapper.ok(
            array)

        form_of_payment_service = FormOfPaymentService(
            self.mock_form_of_payment_repository)

        result = form_of_payment_service.delete(
            "1bceb9a1-5765-4f15-9896-b0c8b3a016c1")

        self.assertEqual(result.IsSuccess, True)
        self.assertEqual(result.Data, "not exist register with this movie_id")

    def test_delete_with_error_first_element(self):
        array = []

        form_of_payment_dto1 = FormOfPaymentDTO(
            id="ef037304-3fe5-41e3-b088-c00aad03c7bd", formName=None, price=None, movieId=None).to_dict()

        form_of_payment_dto2 = FormOfPaymentDTO(
            id="bbee5ce5-390b-43e5-ace6-1ae716c57592", formName=None, price=None, movieId=None).to_dict()

        array.append(form_of_payment_dto1)
        array.append(form_of_payment_dto2)

        self.mock_form_of_payment_repository.get_all_form_of_payment_id_by_movie_id.return_value = ResponseWrapper.ok(
            array)

        self.mock_form_of_payment_repository.delete.side_effect = [
            ResponseWrapper.fail("fail delete payment"),
            ResponseWrapper.ok("Delete successfully")
        ]

        form_of_payment_service = FormOfPaymentService(
            self.mock_form_of_payment_repository)

        result = form_of_payment_service.delete(
            "1bceb9a1-5765-4f15-9896-b0c8b3a016c1")

        self.assertEqual(result.IsSuccess, False)
        self.assertEqual(
            result.Data["message"], "error when delete register from movie_region_tickets_purchesed")

    def test_delete_with_error_second_element(self):
        array = []

        form_of_payment_dto1 = FormOfPaymentDTO(
            id="ef037304-3fe5-41e3-b088-c00aad03c7bd", formName=None, price=None, movieId=None).to_dict()

        form_of_payment_dto2 = FormOfPaymentDTO(
            id="bbee5ce5-390b-43e5-ace6-1ae716c57592", formName=None, price=None, movieId=None).to_dict()

        array.append(form_of_payment_dto1)
        array.append(form_of_payment_dto2)

        self.mock_form_of_payment_repository.get_all_form_of_payment_id_by_movie_id.return_value = ResponseWrapper.ok(
            array)

        self.mock_form_of_payment_repository.delete.side_effect = [
            ResponseWrapper.ok("Delete successfully"),
            ResponseWrapper.fail("fail delete payment")
        ]

        form_of_payment_service = FormOfPaymentService(
            self.mock_form_of_payment_repository)

        result = form_of_payment_service.delete(
            "1bceb9a1-5765-4f15-9896-b0c8b3a016c1")

        self.assertEqual(result.IsSuccess, False)
        self.assertEqual(
            result.Data["message"], "error when delete register from movie_region_tickets_purchesed")
