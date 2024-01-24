from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IUserRepository import IUserRepository
from src.infradata.Context.ApplicationDbContext import ApplicationDbContext
from sqlalchemy.exc import SQLAlchemyError
from src.infradata.Maps.UserMap import UserMap
from src.application.DTOs.UserDTO import UserDTO


class UserRepository(IUserRepository):

    @classmethod
    def get_user_email(cls, email: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                user = (
                    database.session
                    .query(UserMap.Id, UserMap.Name)
                    .filter(UserMap.Email == email)
                    .first()
                )
                database.session.commit()
                return ResponseWrapper.ok(user)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def get_user_by_email(cls, email: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                user = (
                    database.session
                    .query(UserMap.Id, UserMap.Name, UserMap.Email, UserMap.Cpf, UserMap.PasswordHash)
                    .filter(UserMap.Email == email)
                    .first()
                )
                database.session.commit()
                return ResponseWrapper.ok(user)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def get_user_by_email_only_password_hash(cls, idGuid: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                user = (
                    database.session
                    .query(UserMap.PasswordHash)
                    .filter(UserMap.Id == idGuid)
                    .first()
                )
                database.session.commit()
                return ResponseWrapper.ok(user)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def get_user_by_id(cls, idGuid: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                user = (
                    database.session
                    .query(UserMap)
                    .filter(UserMap.Id == idGuid)
                    .first()
                )
                userDb = user.to_dict()
                # print(userDb)
                # print(userDb['Name'])
                # userDTO = UserMap(userDb['name']).to_dict()
                # print(userDTO)
                database.session.commit()
                return ResponseWrapper.ok(userDb)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def get_user_by_cpf(cls, cpf: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                user = (
                    database.session
                    .query(UserMap.Id, UserMap.Email, UserMap.Cpf, UserMap.PasswordHash, UserMap.Name)
                    .filter(UserMap.Cpf == cpf)
                    .first()
                )
                database.session.commit()
                return ResponseWrapper.ok(user)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def check_user_exists(cls, email: str, cpf: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                user = (
                    database.session
                    .query(UserMap.Id, UserMap.Name)
                    .filter(UserMap.Email == email or UserMap.Cpf == cpf)
                    .first()
                )
                database.session.commit()
                return ResponseWrapper.ok(user)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def create_async(cls, user: UserMap) -> ResponseWrapper:
        with ApplicationDbContext() as database:

            userDTO = UserDTO(user.Id, user.Name, user.Email,
                              None, None, None, None).to_dict()

            try:
                database.session.begin()
                database.session.add(user)
                database.session.commit()
                return ResponseWrapper.ok(userDTO)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def update_user_confirm_email(cls, id_user: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                existing_user = database.session.query(UserMap).get(id_user)
                if existing_user != None:
                    existing_user.ConfirmEmail = 1
                database.session.commit()
                return ResponseWrapper.ok("ok")
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")
