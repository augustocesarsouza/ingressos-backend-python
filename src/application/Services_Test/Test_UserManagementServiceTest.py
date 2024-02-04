import unittest
from unittest.mock import Mock
from src.application.DTOs.AdditionalInfoUserDTO import AdditionalInfoUserDTO
from src.application.DTOs.UserDTO import UserDTO
from src.application.Services.Interfaces.IAdditionalInfoUserService import IAdditionalInfoUserService
from src.application.Services.ResponseWrapper import ResponseWrapper

from src.application.Services.UserManagementService import UserManagementService
from src.domain.repositories.IUserRepository import IUserRepository
from src.infradata.SendEmailUser.Interface.ISendEmailUser import ISendEmailUser


class Test_UserManagementServiceTest(unittest.TestCase):

    def test_create_async_user_without_error(self):
        user_repository = Mock(spec=IUserRepository)
        send_email_user = Mock(spec=ISendEmailUser)
        additional_info_user_service = Mock(spec=IAdditionalInfoUserService)

        user_repository.check_user_exists.return_value = ResponseWrapper.fail(
            "não existe")

        user_repository.create_async.return_value = ResponseWrapper.ok(
            "tudo certo")

        user_management_service = UserManagementService(
            user_repository, send_email_user, additional_info_user_service)

        user_DTO = UserDTO(
            None, "augusto", "augusto@gmail.com", "987345875876", None, 0, None, "05/10/1999")

        additional_info_user_DTO = AdditionalInfoUserDTO(
            None,
            None,
            None,
            "05/10/1999",
            "gender",
            "phone",
            "cep",
            "logradouro",
            "numero",
            "complemento",
            "referencia",
            "bairro",
            "estado",
            "cidade"
        )
        password = "login123"

        response = user_management_service.create_async(
            user_DTO, additional_info_user_DTO, password)

        self.assertEqual(response.IsSuccess, True)

    def test_create_async_user_with_error_email_invalid(self):
        user_repository = Mock(spec=IUserRepository)
        send_email_user = Mock(spec=ISendEmailUser)
        additional_info_user_service = Mock(spec=IAdditionalInfoUserService)

        user_management_service = UserManagementService(
            user_repository, send_email_user, additional_info_user_service)

        user_DTO = UserDTO(
            None, "augusto", "augusto", "987345875876", None, 0, None, "05/10/1999")

        response = user_management_service.create_async(
            user_DTO, None, None)

        self.assertEqual(response.IsSuccess, False)

    def test_create_async_user_already_exist(self):
        user_repository = Mock(spec=IUserRepository)
        send_email_user = Mock(spec=ISendEmailUser)
        additional_info_user_service = Mock(spec=IAdditionalInfoUserService)

        user_repository.check_user_exists.return_value = ResponseWrapper.ok(
            "Usuario existe")

        user_management_service = UserManagementService(
            user_repository, send_email_user, additional_info_user_service)

        user_DTO = UserDTO(
            None, "augusto", "augusto@gmail.com", "987345875876", None, 0, None, "05/10/1999")

        response = user_management_service.create_async(
            user_DTO, None, None)

        self.assertEqual(response.IsSuccess, False)

    def test_create_async_error_to_create_repository(self):
        user_repository = Mock(spec=IUserRepository)
        send_email_user = Mock(spec=ISendEmailUser)
        additional_info_user_service = Mock(spec=IAdditionalInfoUserService)

        user_repository.check_user_exists.return_value = ResponseWrapper.fail(
            "não existe")

        user_repository.create_async.return_value = ResponseWrapper.fail(
            "erro ao criar")

        user_management_service = UserManagementService(
            user_repository, send_email_user, additional_info_user_service)

        user_DTO = UserDTO(
            None, "augusto", "augusto@gmail.com", "987345875876", None, 0, None, "05/10/1999")

        password = "login123"

        response = user_management_service.create_async(
            user_DTO, None, password)

        self.assertEqual(response.IsSuccess, False)
