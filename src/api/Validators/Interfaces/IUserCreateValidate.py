from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class IUserCreateValidate(ABC):

    @abstractmethod
    def user_create_validate(cls, body: any) -> ResponseWrapper:
        pass
