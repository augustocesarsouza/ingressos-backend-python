from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.Authentication.ITokenGeneratorEmail import ITokenGeneratorEmail
from src.infradata.Maps.UserMap import UserMap
from src.infradata.Maps.UserPermissionMap import UserPermissionMap
import jwt
from datetime import datetime, timedelta
from src.infradata.Config.JwtConfigFile import jwt_config
import time


class TokenGeneratorEmail(ITokenGeneratorEmail):
    def generator(cls, user: UserMap, userPermissions: list[UserPermissionMap], password: str) -> ResponseWrapper:
        string_join = ""
        for el in userPermissions:
            string_join += el["PermissionName"]
            if len(userPermissions) > 1:
                string_join += ","

        EXP_TIME_MIN = jwt_config["EXP_TIME_MIN"]
        TOKEN_KEY = jwt_config["TOKEN_KEY"]

        token = jwt.encode({
            'exp': datetime.utcnow() + timedelta(minutes=EXP_TIME_MIN),
            'Email': user.Email,
            "Password": password,
            "userID": user.Id,
            "Permissioes": string_join
        }, key=TOKEN_KEY, algorithm="HS256")

        if not len(token) > 0:
            return ResponseWrapper.fail("Error to create token")

        return ResponseWrapper.ok(token)

    # def verficy_token_valid(cls, token: str) -> ResponseWrapper:
    #     TOKEN_KEY = jwt_config["TOKEN_KEY"]
    #     REFRESH_TIME_MIN = jwt_config["REFRESH_TIME_MIN"]

    #     token_information = jwt.decode(
    #         token, key=TOKEN_KEY, algorithms="HS256")
    #     token_userID = token_information["userID"]
    #     exp_time = token_information["exp"]

    #     if ((exp_time - time.time()) / 60) < REFRESH_TIME_MIN:
    #         return ResponseWrapper.fail("token vencido")

    #     return ResponseWrapper.ok("tudo certo")
