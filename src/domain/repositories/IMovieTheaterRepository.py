from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class IMovieTheaterRepository(ABC):

    @abstractmethod
    def get_by_id(cls, movie_theater_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_by_movie_id(cls, id_movie: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def delete(cls, movie_theater_id: str) -> ResponseWrapper:
        pass
