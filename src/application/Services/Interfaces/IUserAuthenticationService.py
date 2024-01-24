from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class IUserAuthenticationService(ABC):

    @abstractmethod
    def login(cls, cpfOrEmail: str, password: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def verfic_token(cls, code: str, guidId: str) -> ResponseWrapper:
        pass
