import unittest
from unittest.mock import patch

from src.infradata.Authentication.TokenGeneratorEmail import TokenGeneratorEmail


class UserMock():
    def __init__(self, id: str = None, name: str = None, email: str = None, cpf: str = None, passwordHash: str = None, confirmEmail: int = None) -> None:
        self.Id = id
        self.Name = name
        self.Email = email
        self.Cpf = cpf
        self.PasswordHash = passwordHash
        self.ConfirmEmail = confirmEmail


class TokenGeneratorEmailTest(unittest.TestCase):

    def test_generator_without_error(self):
        user = UserMock(id="39286a14-h461-4fc0-a828-e459c1d7hc9f",
                        name=None, email="augusto@gmail.com", cpf=None, passwordHash=None, confirmEmail=None)
        password = "senha123456789"
        permissions = [{'Id': 3, 'UserId': '39286a14-h461-4fc0-a828-e459c1d7hc9f',
                        'VisualName': 'administrator', 'PermissionName': 'admin'}]

        user_management_service = TokenGeneratorEmail()

        response = user_management_service.generator(
            user, permissions, password)

        self.assertEqual(response.IsSuccess, True)

    @patch('src.infradata.Authentication.TokenGeneratorEmail.jwt.encode', return_value='')
    def test_generator_with_empty_token(self, mock_jwt_encode):
        user = UserMock(id="39286a14-h461-4fc0-a828-e459c1d7hc9f",
                        name=None, email="augusto@gmail.com", cpf=None, passwordHash=None, confirmEmail=None)
        password = "senha123456789"
        permissions = [{'Id': 3, 'UserId': '39286a14-h461-4fc0-a828-e459c1d7hc9f',
                        'VisualName': 'administrator', 'PermissionName': 'admin'}]

        user_management_service = TokenGeneratorEmail()

        response = user_management_service.generator(
            user, permissions, password)

        self.assertEqual(response.IsSuccess, False)
        self.assertEqual(response.Data["message"], "Error to create token")
