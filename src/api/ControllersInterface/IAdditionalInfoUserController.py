from abc import ABC, abstractmethod
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.HttpTypes.HttpResponse import HttpResponse


class IAdditionalInfoUserController(ABC):

    @abstractmethod
    def get_info_user(cls, http_request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def update_async(cls, http_request: HttpRequest) -> HttpResponse:
        pass
