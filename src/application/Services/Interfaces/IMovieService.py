from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.application.DTOs.MovieDTO import MovieDTO


class IMovieService(ABC):

    @abstractmethod
    def get_movie_by_id_check_exist(self, movie_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_all_movie_by_region_id(self, state: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_info_movies_by_id(self, id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_status_movie(self, status_movie: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def create(self, movie_DTO: MovieDTO) -> ResponseWrapper:
        pass

    @abstractmethod
    def delete_movie(self, id_movie: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def update_movie(self, movie_DTO: MovieDTO) -> ResponseWrapper:
        pass
