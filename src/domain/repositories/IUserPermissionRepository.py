from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class IUserPermissionRepository(ABC):

    @abstractmethod
    def get_all_permission_user(idUser: str) -> ResponseWrapper:
        pass
