from abc import ABC, abstractmethod
from src.application.DTOs.CinemaMovieDTO import CinemaMovieDTO
from src.application.Services.ResponseWrapper import ResponseWrapper


class ICinemaMovieService(ABC):

    @abstractmethod
    def get_by_region_cinema_id_and_movie_id(cls, city_name: str, movie_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def create(cls, cinema_movie_dto: CinemaMovieDTO) -> ResponseWrapper:
        pass

    @abstractmethod
    def delete(cls, movie_id: str) -> ResponseWrapper:
        pass
