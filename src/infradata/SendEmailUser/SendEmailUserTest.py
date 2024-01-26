import unittest
from unittest.mock import Mock, patch
from src.application.Services.ResponseWrapper import ResponseWrapper

from src.infradata.SendEmailUser.SendEmailUser import SendEmailUser
from src.infradata.UtilityExternal.Interface.ICacheRedisUti import ICacheRedisUti
from src.infradata.UtilityExternal.Interface.ISendEmailBrevo import ISendEmailBrevo


class SendEmailUserTest(unittest.TestCase):

    def test_send_email_without_error(self):
        mock_cache_redis = Mock(spec=ICacheRedisUti)
        mock_send_email_brevo = Mock(spec=ISendEmailBrevo)

        mock_send_email_brevo.send_email.return_value = ResponseWrapper.ok(
            "tudo certo")

        send_email_user = SendEmailUser(
            mock_cache_redis, mock_send_email_brevo)

        user = {'id': "39286a14-h461-4fc0-a828-e459c1d7hc9f"}

        response = send_email_user.send_email(user)

        self.assertEqual(response.IsSuccess, True)

    @patch('src.infradata.Authentication.TokenGeneratorEmail.jwt.encode', return_value='')
    def test_send_email_with_empty_token(self, mock_jwt_encode):
        mock_cache_redis = Mock(spec=ICacheRedisUti)
        mock_send_email_brevo = Mock(spec=ISendEmailBrevo)

        user = {'id': "39286a14-h461-4fc0-a828-e459c1d7hc9f"}

        send_email_user = SendEmailUser(
            mock_cache_redis, mock_send_email_brevo)

        response = send_email_user.send_email(user)

        self.assertEqual(response.IsSuccess, False)
        self.assertEqual(response.Data["message"], "Error to create token")
