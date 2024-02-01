from abc import ABC, abstractmethod

from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.HttpTypes.HttpResponse import HttpResponse


class ITheatreController(ABC):

    @abstractmethod
    def get_all_theatre_by_state_name(cls, http_request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def create(cls, http_request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def delete(cls, http_request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def update(cls, http_request: HttpRequest) -> HttpResponse:
        pass
