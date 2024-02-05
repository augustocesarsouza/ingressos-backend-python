from abc import ABC, abstractmethod
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.HttpTypes.HttpResponse import HttpResponse


class IMovieController(ABC):

    @abstractmethod
    def get_all_movie_by_region_id(cls, http_request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def get_info_movies_by_id(cls, http_request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def get_status_movie(cls, http_request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def create(cls, http_request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def delete_movie(cls, http_request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def update_movie(cls, http_request: HttpRequest) -> HttpResponse:
        pass
