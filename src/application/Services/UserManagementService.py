from src.application.Services.Interfaces.IUserManagementService import IUserManagementService
from src.domain.repositories.IUserRepository import IUserRepository
from src.application.Services.ResponseWrapper import ResponseWrapper
import uuid
import hashlib
from src.infradata.Maps.UserMap import UserMap
from src.infradata.SendEmailUser.Interface.ISendEmailUser import ISendEmailUser


class UserManagementService(IUserManagementService):
    def __init__(self, user_repository: IUserRepository, send_email_user: ISendEmailUser) -> None:
        self.__user_repository = user_repository
        self.__send_email_user = send_email_user

    def create_async(self, name: str, email: str, cpf: str, password: str) -> ResponseWrapper:
        userAlreadyCreate = self.__user_repository.check_user_exists(
            email, cpf)

        if not email.__contains__("@gmail.com") and not email.__contains__("@hotmal.com"):
            return ResponseWrapper.fail("email need @gmail.com or @hotmal.com")

        if userAlreadyCreate.Data != None:
            return ResponseWrapper.fail("email or cpf already exist")

        new_guid = uuid.uuid4()
        guid_str = str(new_guid)

        password_hash = self.__generar_hash_password(password)

        # aqui vai faltar 'AdditionalInfoUserDTO' criar a tabela e tals com inforamções adicionar fazer depois

        userMap = UserMap(
            Id=guid_str,
            Name=name,
            Email=email,
            Cpf=cpf,
            PasswordHash=password_hash,
            ConfirmEmail=0
        )

        result = self.__user_repository.create_async(userMap)

        if not result.IsSuccess:
            return result

        self.__send_email_user.send_email(result.Data)

        return result

    def __generar_hash_password(cls, password: str) -> str:
        h = hashlib.new("SHA256")
        # corrent_password = "MyPassword123567"
        h.update(password.encode())

        password_hash = h.hexdigest()  # <- isso guardar no banco de dados
        return password_hash
