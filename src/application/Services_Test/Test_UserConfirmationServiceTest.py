import unittest
from unittest.mock import Mock
from src.application.Services.ResponseWrapper import ResponseWrapper

from src.application.Services.UserConfirmationService import UserConfirmationService
from src.domain.repositories.IUserRepository import IUserRepository
from src.infradata.UtilityExternal.Interface.ICacheRedisUti import ICacheRedisUti
import jwt
from datetime import datetime, timedelta, timezone


class Test_UserConfirmationServiceTest(unittest.TestCase):

    def test_get_confirm_token_without_error(self):
        mock_user_repository = Mock(spec=IUserRepository)
        mock_cache_redis = Mock(spec=ICacheRedisUti)

        token = jwt.encode({
            'exp': datetime.now(timezone.utc) + timedelta(minutes=10),
            "id": "ge61g4f9-165b-4637-a03b-b9d46dcg69b8",
        }, key="seilakey123seilakey", algorithm="HS256")

        mock_cache_redis.get_string_async_wrapper.return_value = "seila"

        mock_user_repository.update_user_confirm_email.return_value = ResponseWrapper.ok(
            "ok")

        user_confirmation_service = UserConfirmationService(
            mock_user_repository, mock_cache_redis)

        response = user_confirmation_service.get_confirm_token(
            token)

        self.assertEqual(response.IsSuccess, True)

    def test_get_confirm_token_with_error_token_invalid_expired(self):
        mock_user_repository = Mock(spec=IUserRepository)
        mock_cache_redis = Mock(spec=ICacheRedisUti)

        token_expired = jwt.encode({
            'exp': datetime.now(timezone.utc) + timedelta(microseconds=1),
            "id": "ge61g4f9-165b-4637-a03b-b9d46dcg69b8",
        }, key="seilakey123seilakey", algorithm="HS256")

        user_confirmation_service = UserConfirmationService(
            mock_user_repository, mock_cache_redis)

        response = user_confirmation_service.get_confirm_token(
            token_expired)

        self.assertEqual(response.IsSuccess, False)
        self.assertEqual(response.Data['message'], "Token Expirou")

    def test_get_confirm_token_with_error_token_invalid(self):
        mock_user_repository = Mock(spec=IUserRepository)
        mock_cache_redis = Mock(spec=ICacheRedisUti)

        token_invalid = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDYyMDQ0MjgsImlkIjoiYmUxZjgxNGYtM2QwOS00ZmExLWI5MTktMjg5NzJkMmI3Y2U1In0.iKfgMt9EA1o3eYczACBuqGKtLaOOfY1Yuuy7rlfnkS"

        user_confirmation_service = UserConfirmationService(
            mock_user_repository, mock_cache_redis)

        response = user_confirmation_service.get_confirm_token(
            token_invalid)

        self.assertEqual(response.IsSuccess, False)
        self.assertEqual(response.Data['message'], "Token Invalido")

    def test_get_confirm_token_with_error_token_id_attribute_not_found(self):
        mock_user_repository = Mock(spec=IUserRepository)
        mock_cache_redis = Mock(spec=ICacheRedisUti)

        token_without_attribute_id = jwt.encode({
            'exp': datetime.now(timezone.utc) + timedelta(minutes=10),
            # "id": "ge61g4f9-165b-4637-a03b-b9d46dcg69b8",
        }, key="seilakey123seilakey", algorithm="HS256")

        user_confirmation_service = UserConfirmationService(
            mock_user_repository, mock_cache_redis)

        response = user_confirmation_service.get_confirm_token(
            token_without_attribute_id)

        self.assertEqual(response.IsSuccess, False)
        self.assertEqual(response.Data['message'], "Token Invalido2")

    def test_get_confirm_token_with_error_token_exp_attribute_not_found(self):
        mock_user_repository = Mock(spec=IUserRepository)
        mock_cache_redis = Mock(spec=ICacheRedisUti)

        token_without_attribute_id = jwt.encode({
            # 'exp': datetime.utcnow() + timedelta(minutes=10),
            "id": "ge61g4f9-165b-4637-a03b-b9d46dcg69b8",
        }, key="seilakey123seilakey", algorithm="HS256")

        user_confirmation_service = UserConfirmationService(
            mock_user_repository, mock_cache_redis)

        response = user_confirmation_service.get_confirm_token(
            token_without_attribute_id)

        self.assertEqual(response.IsSuccess, False)
        self.assertEqual(response.Data['message'], "Token Invalido2")

    def test_get_confirm_token_with_error_token_id_attribute_less_than_36(self):
        mock_user_repository = Mock(spec=IUserRepository)
        mock_cache_redis = Mock(spec=ICacheRedisUti)

        token_without_attribute_id = jwt.encode({
            'exp': datetime.now(timezone.utc) + timedelta(minutes=10),
            "id": "ge61g4f9-165b-4637-a03b-b9d46dcg69b",
        }, key="seilakey123seilakey", algorithm="HS256")

        user_confirmation_service = UserConfirmationService(
            mock_user_repository, mock_cache_redis)

        response = user_confirmation_service.get_confirm_token(
            token_without_attribute_id)

        self.assertEqual(response.IsSuccess, False)
        self.assertEqual(response.Data['message'], "erro id do usuario token")

    def test_get_confirm_token_token_already_visualized(self):
        mock_user_repository = Mock(spec=IUserRepository)
        mock_cache_redis = Mock(spec=ICacheRedisUti)

        token = jwt.encode({
            'exp': datetime.now(timezone.utc) + timedelta(minutes=10),
            "id": "ge61g4f9-165b-4637-a03b-b9d46dcg69b8",
        }, key="seilakey123seilakey", algorithm="HS256")

        mock_cache_redis.get_string_async_wrapper.return_value = None

        user_confirmation_service = UserConfirmationService(
            mock_user_repository, mock_cache_redis)

        response = user_confirmation_service.get_confirm_token(
            token)

        self.assertEqual(response.IsSuccess, True)
        self.assertEqual(response.Data["tokenAlreadyVisualized"], True)
        self.assertEqual(response.Data["erroMessage"], "já Visualizado")
