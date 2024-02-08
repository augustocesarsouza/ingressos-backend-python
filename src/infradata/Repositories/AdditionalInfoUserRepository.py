from src.application.DTOs.AdditionalInfoUserDTO import AdditionalInfoUserDTO
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IAdditionalInfoUserRepository import IAdditionalInfoUserRepository
from src.infradata.Context.ApplicationDbContext import ApplicationDbContext
from src.infradata.Maps.AdditionalInfoUserMap import AdditionalInfoUserMap
from sqlalchemy.exc import SQLAlchemyError


class AdditionalInfoUserRepository(IAdditionalInfoUserRepository):

    @classmethod
    def get_info_user(self, id_guid: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                additional = (
                    database.session
                    .query(AdditionalInfoUserMap.BirthDate, AdditionalInfoUserMap.Gender, AdditionalInfoUserMap.Phone, AdditionalInfoUserMap.Cep, AdditionalInfoUserMap.Logradouro, AdditionalInfoUserMap.Numero, AdditionalInfoUserMap.Complemento, AdditionalInfoUserMap.Referencia, AdditionalInfoUserMap.Bairro, AdditionalInfoUserMap.Estado, AdditionalInfoUserMap.Cidade)
                    .filter(AdditionalInfoUserMap.UserId == id_guid)
                    .first()
                )
                database.session.commit()

                if additional != None:
                    additionalInfoUserDTO = AdditionalInfoUserDTO(id=None, userId=None, birthDate=additional.BirthDate, birthDateString=None, gender=additional.Gender, phone=additional.Phone, logradouro=additional.Logradouro,
                                                                  numero=additional.Numero, complemento=additional.Complemento, referencia=additional.Referencia, bairro=additional.Bairro, estado=additional.Estado, cidade=additional.Cidade).to_dict()

                    return ResponseWrapper.ok(additionalInfoUserDTO)
                else:
                    return ResponseWrapper.ok(additional)

            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def get_by_id_guid_user(self, id_guid: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                user = (
                    database.session
                    .query(AdditionalInfoUserMap)
                    .filter(AdditionalInfoUserMap.UserId == id_guid)
                    .first()
                )
                database.session.commit()
                return ResponseWrapper.ok(user)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def create_info(self, infoUser: AdditionalInfoUserMap) -> ResponseWrapper:
        with ApplicationDbContext() as database:

            additionalInfoUserDTO = AdditionalInfoUserDTO(None, None, infoUser.BirthDate, None, infoUser.Gender, infoUser.Phone, infoUser.Cep, infoUser.Logradouro,
                                                          infoUser.Numero, infoUser.Complemento, infoUser.Referencia, infoUser.Bairro, infoUser.Estado, infoUser.Cidade).to_dict()

            try:
                database.session.begin()
                database.session.add(infoUser)
                database.session.commit()
                return ResponseWrapper.ok(additionalInfoUserDTO)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def update_async(self, infoUser: AdditionalInfoUserDTO) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                existing_user = database.session.query(
                    AdditionalInfoUserMap).filter(AdditionalInfoUserMap.UserId == infoUser.UserId).first()

                if existing_user != None:
                    existing_user.BirthDate = infoUser.BirthDate
                    existing_user.Gender = infoUser.Gender
                    existing_user.Phone = infoUser.Phone
                    existing_user.Cep = infoUser.Cep
                    existing_user.Logradouro = infoUser.Logradouro
                    existing_user.Numero = infoUser.Numero
                    existing_user.Complemento = infoUser.Complemento
                    existing_user.Referencia = infoUser.Referencia
                    existing_user.Bairro = infoUser.Bairro
                    existing_user.Estado = infoUser.Estado
                    existing_user.Cidade = infoUser.Cidade
                database.session.commit()
                return ResponseWrapper.ok("ok")
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")
