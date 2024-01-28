from abc import ABC, abstractmethod
from src.application.DTOs.MovieDTO import MovieDTO
from src.application.Services.ResponseWrapper import ResponseWrapper

from src.infradata.Maps.MovieMap import MovieMap


class IMovieRepository(ABC):

    @abstractmethod
    def get_by_id(cls, id_movie: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_info_movies_by_id(cls, id_movie: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_status_movie(cls, status_movie: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_by_id_all_props(cls, id_movie: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_all_movie_by_region_id(cls, region_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def create(cls, movie: MovieMap) -> ResponseWrapper:
        pass

    @abstractmethod
    def delete(cls, id_movie: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def update_movie(cls, movie_DTO: MovieDTO) -> ResponseWrapper:
        pass
