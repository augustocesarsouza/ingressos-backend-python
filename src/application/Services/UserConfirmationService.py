from src.application.DTOs.TokenAlreadyVisualizedDTO import TokenAlreadyVisualizedDTO
from src.application.Services.Interfaces.IUserConfirmationService import IUserConfirmationService
import jwt
import time
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IUserRepository import IUserRepository
from src.infradata.Maps.UserMap import UserMap
from src.infradata.UtilityExternal.Interface.ICacheRedisUti import ICacheRedisUti


class UserConfirmationService(IUserConfirmationService):
    def __init__(self, user_repository: IUserRepository, cache_redis: ICacheRedisUti) -> None:
        self.__cache_redis = cache_redis
        self.__user_repository = user_repository

    def get_confirm_token(self, token: str) -> ResponseWrapper:
        try:
            token_information = jwt.decode(
                token, key="seilakey123seilakey", algorithms="HS256")
            exp_token = token_information["exp"]

            id_user = token_information["id"]
        except jwt.InvalidSignatureError:
            return ResponseWrapper.fail("Token Invalido")
        except jwt.ExpiredSignatureError:
            return ResponseWrapper.fail("Token Expirou")
        except KeyError as e:
            print("Token Invalido2")
            return ResponseWrapper.fail("Token Invalido2")

        time_exp = (exp_token - time.time()) / 60
        if time_exp <= 0:
            return ResponseWrapper.fail("Token Expirou")

        if len(id_user) > 0:
            chave_key = f"TokenString {id_user}"

            cache = self.__cache_redis.get_string_async_wrapper(chave_key)

            if cache != None:
                self.__cache_redis.remove_wrapper(chave_key)
            else:
                # token_DTO = {"TokenAlreadyVisualized": True}
                token_DTO = TokenAlreadyVisualizedDTO(
                    True, "já Visualizado").to_dict()
                return ResponseWrapper.ok(token_DTO)

            # user_result = self.__user_repository.get_user_by_id(id_user)
            user_result = self.__user_repository.update_user_confirm_email(
                id_user)

            return user_result
