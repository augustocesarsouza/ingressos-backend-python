from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class IUserManagementService(ABC):

    @abstractmethod
    def create_async(cls, name: str, email: str, cpf: str, password: str) -> ResponseWrapper:
        pass
