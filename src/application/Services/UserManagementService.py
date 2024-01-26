from src.application.DTOs.AdditionalInfoUserDTO import AdditionalInfoUserDTO
from src.application.DTOs.UserDTO import UserDTO
from src.application.Services.Interfaces.IAdditionalInfoUserService import IAdditionalInfoUserService
from src.application.Services.Interfaces.IUserManagementService import IUserManagementService
from src.domain.repositories.IUserRepository import IUserRepository
from src.application.Services.ResponseWrapper import ResponseWrapper
import uuid
import hashlib
from src.infradata.Maps.AdditionalInfoUserMap import AdditionalInfoUserMap
from src.infradata.Maps.UserMap import UserMap
from src.infradata.SendEmailUser.Interface.ISendEmailUser import ISendEmailUser
from datetime import datetime


class UserManagementService(IUserManagementService):
    def __init__(self, user_repository: IUserRepository, send_email_user: ISendEmailUser, additional_info_user_service: IAdditionalInfoUserService) -> None:
        self.__user_repository = user_repository
        self.__send_email_user = send_email_user
        self.__additional_info_user_service = additional_info_user_service

    def create_async(self, user_DTO: UserDTO, additional_info_user_DTO: AdditionalInfoUserDTO, password: str) -> ResponseWrapper:
        userAlreadyCreate = self.__user_repository.check_user_exists(
            user_DTO.Email, user_DTO.Cpf)

        if not user_DTO.Email.__contains__("@gmail.com") and not user_DTO.Email.__contains__("@hotmal.com"):
            return ResponseWrapper.fail("email need @gmail.com or @hotmal.com")

        if userAlreadyCreate.IsSuccess == True and userAlreadyCreate.Data != None:
            return ResponseWrapper.fail("email or cpf already exist")

        new_guid = uuid.uuid4()
        guid_str = str(new_guid)

        password_hash = self.__generar_hash_password(password)

        userMap = UserMap(
            Id=guid_str,
            Name=user_DTO.Name,
            Email=user_DTO.Email,
            Cpf=user_DTO.Cpf,
            PasswordHash=password_hash,
            ConfirmEmail=0
        )

        result_create_user = self.__user_repository.create_async(userMap)

        if not result_create_user.IsSuccess:
            return result_create_user

        self.__send_email_user.send_email(result_create_user.Data)

        if result_create_user.IsSuccess:
            self.__create_user_additional_info(
                user_DTO.BirthDateString, additional_info_user_DTO, guid_str)

        return result_create_user

    def __generar_hash_password(cls, password: str) -> str:
        h = hashlib.new("SHA256")
        h.update(password.encode())

        password_hash = h.hexdigest()  # <- isso guardar no banco de dados
        return password_hash

    def __create_user_additional_info(self, birth_date_string: str, additional_info_user_DTO: AdditionalInfoUserDTO, guid_str: str):
        parts = birth_date_string.split('/')

        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])

        birth_date = datetime(year, month, day)
        additional_info_user_DTO.set_birth_date(birth_date)
        additional_info_user_DTO.set_user_id(guid_str)

        self.__additional_info_user_service.create_info(
            additional_info_user_DTO)
