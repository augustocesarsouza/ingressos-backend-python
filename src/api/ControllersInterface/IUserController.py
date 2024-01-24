from abc import ABC, abstractmethod
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.HttpTypes.HttpResponse import HttpResponse


class IUserController(ABC):

    @abstractmethod
    def create_async(self, http_request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def login_user(self, http_request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def verfic_token(self, http_request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def get_confirm_token(self, http_request: HttpRequest) -> HttpResponse:
        pass
