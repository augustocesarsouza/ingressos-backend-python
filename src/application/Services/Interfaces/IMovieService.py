from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.application.DTOs.MovieDTO import MovieDTO


class IMovieService(ABC):

    @abstractmethod
    def get_movie_by_id_check_exist(cls, movie_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_all_movie_by_region_id(cls, state: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_info_movies_by_id(cls, id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_status_movie(cls, status_movie: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def create(cls, movie_DTO: MovieDTO) -> ResponseWrapper:
        pass

    @abstractmethod
    def delete_movie(cls, id_movie: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def update_movie(cls, movie_DTO: MovieDTO) -> ResponseWrapper:
        pass
