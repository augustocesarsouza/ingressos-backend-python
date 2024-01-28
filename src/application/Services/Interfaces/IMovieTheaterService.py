from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class IMovieTheaterService(ABC):

    @abstractmethod
    def get_by_id_movie(cls, movie_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def delete(cls, movie_id: str) -> ResponseWrapper:
        pass
