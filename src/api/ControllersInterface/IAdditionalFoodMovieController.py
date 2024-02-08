from abc import ABC, abstractmethod
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.HttpTypes.HttpResponse import HttpResponse


class IAdditionalFoodMovieController(ABC):

    @abstractmethod
    def get_all_food_movie(cls, http_request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def create(cls, http_request: HttpRequest) -> HttpResponse:
        pass
