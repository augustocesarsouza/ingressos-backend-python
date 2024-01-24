from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.infradata.Maps.UserMap import UserMap


class IUserRepository(ABC):

    @abstractmethod
    def get_user_email(cls, email: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_user_by_email(cls, email: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_user_by_email_only_password_hash(cls, idGuid: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_user_by_id(cls, idGuid: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_user_by_cpf(cls, cpf: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def check_user_exists(cls, email: str, cpf: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def create_async(cls, user: UserMap) -> ResponseWrapper:
        pass

    @abstractmethod
    def update_user_confirm_email(cls, id_user: str) -> ResponseWrapper:
        pass
