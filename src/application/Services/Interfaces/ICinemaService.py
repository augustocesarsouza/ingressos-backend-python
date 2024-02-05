from abc import ABC, abstractmethod
from src.application.DTOs.CinemaDTO import CinemaDTO
from src.application.Services.ResponseWrapper import ResponseWrapper


class ICinemaService(ABC):

    @abstractmethod
    def get_cinema_by_id_check_exist(cls, cinema_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def create(cls, cinema_dto: CinemaDTO) -> ResponseWrapper:
        pass
