from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.infradata.Maps.UserMap import UserMap
from src.infradata.Maps.UserPermissionMap import UserPermissionMap


class ITokenGeneratorEmail(ABC):

    @abstractmethod
    def generator(cls, user: UserMap, userPermissions: list[UserPermissionMap], password: str) -> ResponseWrapper:
        pass

    # @abstractmethod
    # def verficy_token_valid(cls, token: str) -> ResponseWrapper:
    #     pass
