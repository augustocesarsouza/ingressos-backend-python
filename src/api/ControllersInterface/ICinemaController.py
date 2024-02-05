from abc import ABC, abstractmethod
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.HttpTypes.HttpResponse import HttpResponse


class ICinemaController(ABC):

    @abstractmethod
    def create(cls, http_request: HttpRequest) -> HttpResponse:
        pass
