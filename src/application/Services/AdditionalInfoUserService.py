from src.application.DTOs.AdditionalInfoUserDTO import AdditionalInfoUserDTO
from src.application.Services.Interfaces.IAdditionalInfoUserService import IAdditionalInfoUserService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IAdditionalInfoUserRepository import IAdditionalInfoUserRepository
from src.domain.repositories.IUserRepository import IUserRepository
from src.infradata.Maps.AdditionalInfoUserMap import AdditionalInfoUserMap
from datetime import datetime
import hashlib


class AdditionalInfoUserService(IAdditionalInfoUserService):
    def __init__(self, additional_info_user_repository: IAdditionalInfoUserRepository, user_repository: IUserRepository) -> None:
        self.__additional_info_user_repository = additional_info_user_repository
        self.__user_repository = user_repository

    def get_info_user(self, id_guid: str) -> ResponseWrapper:
        user_info_result = self.__additional_info_user_repository.get_info_user(
            id_guid)

        return user_info_result

    def create_info(self, infoUser: AdditionalInfoUserDTO) -> ResponseWrapper:
        if infoUser == None:
            return ResponseWrapper.fail("objeto informado é None")

        additional_info_user_map = AdditionalInfoUserMap(
            UserId=infoUser.UserId,
            BirthDate=infoUser.BirthDate,
            Gender=infoUser.Gender,
            Phone=infoUser.Phone,
            Cep=infoUser.Cep,
            Logradouro=infoUser.Logradouro,
            Numero=infoUser.Numero,
            Complemento=infoUser.Complemento,
            Referencia=infoUser.Referencia,
            Bairro=infoUser.Bairro,
            Estado=infoUser.Estado,
            Cidade=infoUser.Cidade
        )

        result_create = self.__additional_info_user_repository.create_info(
            additional_info_user_map)

        return result_create

    def update_async(self, infoUser: AdditionalInfoUserDTO, password: str) -> ResponseWrapper:
        user_validate_hash = self.__user_repository.get_user_by_id(
            infoUser.UserId)

        if user_validate_hash.Data == None:
            return ResponseWrapper.fail("error ao encontrar user")

        user = user_validate_hash.Data
        print(user)

        password_user_send = self.__generar_hash_password(password)
        password_database_hash = user['passwordhash']

        if password_user_send != password_database_hash:
            return ResponseWrapper.fail("Password Invalid")

        parts = infoUser.BirthDateString.split('/')

        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])

        birth_date = datetime(year, month, day)

        infoUser.set_birth_date(birth_date)

        result_update = self.__additional_info_user_repository.update_async(
            infoUser)

        return result_update

    def __generar_hash_password(cls, password: str) -> str:
        h = hashlib.new("SHA256")
        h.update(password.encode())

        password_hash = h.hexdigest()  # <- isso guardar no banco de dados
        return password_hash
