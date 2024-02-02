from abc import ABC, abstractmethod
from src.application.DTOs.CinemaMovieDTO import CinemaMovieDTO
from src.application.Services.ResponseWrapper import ResponseWrapper


class ICinemaMovieService(ABC):

    @abstractmethod
    def get_by_region_cinema_id_and_movie_id(self, city_name: str, movie_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def create(self, cinema_movie_dto: CinemaMovieDTO) -> ResponseWrapper:
        pass
