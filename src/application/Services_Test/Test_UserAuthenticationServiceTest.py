import unittest
from unittest.mock import Mock
from src.api.Validators.Interfaces.IUserCreateValidate import IUserCreateValidate
from src.application.DTOs.UserDTO import UserDTO
from src.application.Services.Interfaces.IUserPermissionService import IUserPermissionService

from src.application.Services.UserAuthenticationService import UserAuthenticationService
from src.domain.Authentication.ITokenGeneratorEmail import ITokenGeneratorEmail
from src.domain.repositories.IUserRepository import IUserRepository
from src.application.Services.ResponseWrapper import ResponseWrapper
import hashlib

from src.infradata.SendEmailUser.Interface.ISendEmailUser import ISendEmailUser


class Test_UserAuthenticationServiceTest(unittest.TestCase):

    def test_login_without_error(self):
        mock_user_repository = Mock(spec=IUserRepository)
        mock_user_permission_service = Mock(spec=IUserPermissionService)
        mock_token_generator_email = Mock(spec=ITokenGeneratorEmail)
        mock_send_email_user = Mock(spec=ISendEmailUser)

        password = "augusto123"

        h = hashlib.new("SHA256")
        h.update(password.encode())

        password_hash = h.hexdigest()

        userDTO = UserDTO("91686h20-e431-4gc0-a828-e612s6d7bc9f", "augusto",
                          "augusto@gmail.com", None, password_hash, None, None, None)

        mock_user_repository.get_user_by_email.return_value = ResponseWrapper.ok(
            userDTO)

        mock_user_permission_service.get_all_permission_user.return_value = ResponseWrapper.ok(
            "tudo certo")

        mock_token_generator_email.generator.return_value = ResponseWrapper.ok(
            "tudo certo")

        user_service = UserAuthenticationService(
            mock_user_repository, mock_user_permission_service, mock_token_generator_email,  mock_send_email_user)

        response = user_service.login("augusto@gmail.com", password)

        self.assertEqual(response.IsSuccess, True)

    def test_login_with_error_user_not_exist(self):
        mock_user_repository = Mock(spec=IUserRepository)
        mock_user_permission_service = Mock(spec=IUserPermissionService)
        mock_token_generator_email = Mock(spec=ITokenGeneratorEmail)
        mock_send_email_user = Mock(spec=ISendEmailUser)

        password = "augusto123"

        mock_user_repository.get_user_by_email.return_value = ResponseWrapper.ok(
            None)

        user_service = UserAuthenticationService(
            mock_user_repository, mock_user_permission_service, mock_token_generator_email,  mock_send_email_user)

        response = user_service.login("augusto@gmail.com", password)

        self.assertEqual(response.IsSuccess, False)

    def test_login_without_error_user_not_have_permissions(self):
        mock_user_repository = Mock(spec=IUserRepository)
        mock_user_permission_service = Mock(spec=IUserPermissionService)
        mock_token_generator_email = Mock(spec=ITokenGeneratorEmail)
        mock_send_email_user = Mock(spec=ISendEmailUser)

        password = "augusto123"

        h = hashlib.new("SHA256")
        h.update(password.encode())

        password_hash = h.hexdigest()

        userDTO = UserDTO("91686h20-e431-4gc0-a828-e612s6d7bc9f", "augusto",
                          "augusto@gmail.com", None, password_hash, None, None, None)

        mock_user_repository.get_user_by_email.return_value = ResponseWrapper.ok(
            userDTO)

        mock_user_permission_service.get_all_permission_user.return_value = ResponseWrapper.fail(
            "error user not have permission")

        user_service = UserAuthenticationService(
            mock_user_repository, mock_user_permission_service, mock_token_generator_email,  mock_send_email_user)

        response = user_service.login("augusto@gmail.com", password)

        self.assertEqual(response.IsSuccess, False)

    def test_login_without_error_when_creating_token(self):
        mock_user_repository = Mock(spec=IUserRepository)
        mock_user_permission_service = Mock(spec=IUserPermissionService)
        mock_token_generator_email = Mock(spec=ITokenGeneratorEmail)
        mock_send_email_user = Mock(spec=ISendEmailUser)

        password = "augusto123"

        h = hashlib.new("SHA256")
        h.update(password.encode())

        password_hash = h.hexdigest()

        userDTO = UserDTO("91686h20-e431-4gc0-a828-e612s6d7bc9f", "augusto",
                          "augusto@gmail.com", None, password_hash, None, None, None)

        mock_user_repository.get_user_by_email.return_value = ResponseWrapper.ok(
            userDTO)

        mock_user_permission_service.get_all_permission_user.return_value = ResponseWrapper.ok(
            "tudo certo")

        mock_token_generator_email.generator.return_value = ResponseWrapper.fail(
            "error when generator token")

        user_service = UserAuthenticationService(
            mock_user_repository, mock_user_permission_service, mock_token_generator_email,  mock_send_email_user)

        response = user_service.login("augusto@gmail.com", password)

        self.assertEqual(response.IsSuccess, False)

    def test_verfic_token_with_error(self):
        mock_user_repository = Mock(spec=IUserRepository)
        mock_user_permission_service = Mock(spec=IUserPermissionService)
        mock_token_generator_email = Mock(spec=ITokenGeneratorEmail)
        mock_send_email_user = Mock(spec=ISendEmailUser)

        user_service = UserAuthenticationService(
            mock_user_repository, mock_user_permission_service, mock_token_generator_email,  mock_send_email_user)

        response = user_service.verfic_token(
            "123456", "3772a3b6-f97a-4619-87fe-4c0aff43f52a")

        self.assertEqual(response.IsSuccess, False)
