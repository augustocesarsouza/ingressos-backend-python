from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.infradata.Maps.CinemaMovieMap import CinemaMovieMap


class ICinemaMovieRepository(ABC):

    @abstractmethod
    def get_by_region_cinema_id_and_movie_id(self, region_id: str, movie_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def create(self, cinema_movie_map: CinemaMovieMap) -> ResponseWrapper:
        pass
