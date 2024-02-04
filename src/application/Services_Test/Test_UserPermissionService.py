import unittest
from unittest.mock import Mock
from src.application.Services.ResponseWrapper import ResponseWrapper

from src.application.Services.UserPermissionService import UserPermissionService
from src.domain.repositories.IUserPermissionRepository import IUserPermissionRepository


class Test_UserPermissionService(unittest.TestCase):

    def test_get_all_permission_user_without_error(self):
        mock_user_permission_repository = Mock(spec=IUserPermissionRepository)

        id_user = "39286a14-h461-4fc0-a828-e459c1d7hc9f"

        permissions = [{'Id': 3, 'UserId': '39286a14-h461-4fc0-a828-e459c1d7hc9f',
                        'VisualName': 'administrator', 'PermissionName': 'admin'}]

        mock_user_permission_repository.get_all_permission_user.return_value = ResponseWrapper.ok(
            permissions)

        user_management_service = UserPermissionService(
            mock_user_permission_repository)

        response = user_management_service.get_all_permission_user(id_user)

        self.assertEqual(response.IsSuccess, True)

    def test_get_all_permission_user_error_not_exist_permissions(self):
        mock_user_permission_repository = Mock(spec=IUserPermissionRepository)

        id_user = "39286a14-h461-4fc0-a828-e459c1d7hc9f"
        permissions = []

        mock_user_permission_repository.get_all_permission_user.return_value = ResponseWrapper.ok(
            permissions)

        user_management_service = UserPermissionService(
            mock_user_permission_repository)

        response = user_management_service.get_all_permission_user(id_user)

        self.assertEqual(response.IsSuccess, False)

    def test_get_all_permission_user_database_error(self):
        mock_user_permission_repository = Mock(spec=IUserPermissionRepository)

        id_user = "39286a14-h461-4fc0-a828-e459c1d7hc9f"

        mock_user_permission_repository.get_all_permission_user.return_value = ResponseWrapper.fail(
            "error database")

        user_management_service = UserPermissionService(
            mock_user_permission_repository)

        response = user_management_service.get_all_permission_user(id_user)

        self.assertEqual(response.IsSuccess, False)
