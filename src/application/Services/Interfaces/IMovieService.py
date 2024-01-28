from abc import ABC, abstractmethod
from src.application.DTOs.MovieDTO import MovieDTO

from src.application.Services.ResponseWrapper import ResponseWrapper


class IMovieService(ABC):

    @abstractmethod
    def get_all_movie_by_region_id(self, region: str) -> ResponseWrapper:
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

    @abstractmethod
    def update_movie_img_background(self, movie_DTO: MovieDTO) -> ResponseWrapper:
        pass
