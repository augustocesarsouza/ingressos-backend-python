from abc import ABC, abstractmethod
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.HttpTypes.HttpResponse import HttpResponse


class IFormOfPaymentController(ABC):

    @abstractmethod
    def get_movie_Id_info(self, http_request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def create(self, http_request: HttpRequest) -> HttpResponse:
        pass
