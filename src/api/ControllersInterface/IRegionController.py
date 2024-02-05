from abc import ABC, abstractmethod

from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.HttpTypes.HttpResponse import HttpResponse


class IRegionController(ABC):

    @abstractmethod
    def get_all_movie_by_region_id(cls, http_request: HttpRequest) -> HttpResponse:
        pass
