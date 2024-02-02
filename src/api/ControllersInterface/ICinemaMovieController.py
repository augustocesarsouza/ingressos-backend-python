from abc import ABC, abstractmethod
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.HttpTypes.HttpResponse import HttpResponse


class ICinemaMovieController(ABC):

    @abstractmethod
    def get_by_region_cinema_id_and_movie_id(self, http_request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def create(self, http_request: HttpRequest) -> HttpResponse:
        pass
