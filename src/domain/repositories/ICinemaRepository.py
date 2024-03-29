from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.infradata.Maps.CinemaMap import CinemaMap


class ICinemaRepository(ABC):

    @abstractmethod
    def create(cls, cinema_map: CinemaMap) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_cinema_by_id_check_exist(cls, cinema_id: str) -> ResponseWrapper:
        pass
