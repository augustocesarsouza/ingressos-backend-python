from abc import ABC, abstractmethod
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.HttpTypes.HttpResponse import HttpResponse


class IMovieRegionTicketsPurchesedController(ABC):

    @abstractmethod
    def get_by_movie_id_and_cinema_id(self, http_request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def create(self, http_request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def update(self, http_request: HttpRequest) -> HttpResponse:
        pass
