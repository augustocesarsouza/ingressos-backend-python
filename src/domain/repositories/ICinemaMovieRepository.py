from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.infradata.Maps.CinemaMovieMap import CinemaMovieMap


class ICinemaMovieRepository(ABC):

    @abstractmethod
    def get_by_region_cinema_id_and_movie_id(cls, region_id: str, movie_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_all_cinema_movie_id_by_movie_id(cls, movie_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def create(cls, cinema_movie_map: CinemaMovieMap) -> ResponseWrapper:
        pass

    @abstractmethod
    def delete(cls, cinema_movie_id: str) -> ResponseWrapper:
        pass
