from src.infradata.SendEmailUser.Interface.ISendEmailUser import ISendEmailUser
from src.infradata.UtilityExternal.Interface.ICacheRedisUti import ICacheRedisUti
from src.infradata.UtilityExternal.Interface.ISendEmailBrevo import ISendEmailBrevo
import jwt
from datetime import datetime, timedelta, timezone
from src.application.Services.ResponseWrapper import ResponseWrapper


class SendEmailUser(ISendEmailUser):
    def __init__(self, cache_redis: ICacheRedisUti, send_email_brevo: ISendEmailBrevo) -> None:
        self.__cache_redis = cache_redis
        self.__send_email_brevo = send_email_brevo

    def send_email(self, user: dict[str, any]) -> ResponseWrapper:
        chave_key = f"TokenString {user['id']}"
        cache = self.__cache_redis.get_string_async_wrapper(chave_key)

        token = jwt.encode({
            'exp': datetime.now(timezone.utc) + timedelta(minutes=10),
            "id": user['id'],
        }, key="seilakey123seilakey", algorithm="HS256")

        if not len(token) > 0:
            return ResponseWrapper.fail("Error to create token")

        if cache == None:
            self.__cache_redis.set_string_async_wrapper_expiry(
                chave_key, token, 600)

        # url = f"http://localhost:6400/minha-conta/confirmacao-de-email?token={token}"
        url = "http://{}:{}/minha-conta/confirmacao-de-email?token={}".format(
            'localhost',
            '6400',
            token
        )

        result_send = self.__send_email_brevo.send_email(user, url)

        return result_send

    def send_code_random(self, user: dict[str, any], code: int) -> ResponseWrapper:
        result_send = self.__send_email_brevo.send_code(user, code)
        return result_send
