from src.application.DTOs.UserDTO import UserDTO
from src.application.Services.Interfaces.IUserAuthenticationService import IUserAuthenticationService
from src.application.Services.Interfaces.IUserPermissionService import IUserPermissionService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.Authentication.ITokenGeneratorEmail import ITokenGeneratorEmail
from src.domain.repositories.IUserRepository import IUserRepository
import hashlib
from src.application.CodeRandomUser.CodeRandomDictionary import code_random_dictionary_instance
import random

from src.infradata.SendEmailUser.Interface.ISendEmailUser import ISendEmailUser


class UserAuthenticationService(IUserAuthenticationService):
    def __init__(self, user_repository: IUserRepository, user_permission_service: IUserPermissionService, token_generator_email: ITokenGeneratorEmail, send_email_user: ISendEmailUser) -> None:
        self.__user_repository = user_repository
        self.__user_permission_service = user_permission_service
        self.__token_generator_email = token_generator_email
        self.__send_email_user = send_email_user

    def login(self, cpfOrEmail: str, password: str) -> ResponseWrapper:
        resultUser = self.__user_repository.get_user_by_email(cpfOrEmail)

        if resultUser.Data == None:
            return ResponseWrapper.fail("user not exists")

        if not resultUser.IsSuccess:
            return resultUser

        user = resultUser.Data

        password_user_send = self.__generar_hash_password(password)
        password_database_hash = user.PasswordHash

        if password_user_send != password_database_hash:
            return ResponseWrapper.fail("Password Invalid")

        response_permissions = self.__user_permission_service.get_all_permission_user(
            user.Id)

        if not response_permissions.IsSuccess:
            return response_permissions

        token_response = self.__token_generator_email.generator(
            user, response_permissions.Data, password)

        if not token_response.IsSuccess:
            return token_response

        userDTO = UserDTO(user.Id, user.Name, user.Email,
                          None, None, None, token_response.Data, None).to_dict()

        randomCode = self.__gerar_numero_aleatorio()
        code_random_dictionary_instance.add(userDTO['id'], randomCode)

        # descomentar se quiser mandar para o email
        # self.__send_email_user.send_code_random(userDTO, randomCode)

        return ResponseWrapper.ok(userDTO)

    def verfic_token(cls, code: str, guidId: str) -> ResponseWrapper:
        if code_random_dictionary_instance.container(guidId, code):
            code_random_dictionary_instance.remove(guidId)
            return ResponseWrapper.ok("Ok")
        else:
            return ResponseWrapper.fail("error")

    def __generar_hash_password(cls, password: str) -> str:
        h = hashlib.new("SHA256")
        h.update(password.encode())

        password_hash = h.hexdigest()  # <- isso guardar no banco de dados
        return password_hash

    def __gerar_numero_aleatorio(cls) -> int:
        return random.randint(100000, 999999)
