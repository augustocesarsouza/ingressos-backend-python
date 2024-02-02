from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class ICinemaMovieValidate(ABC):

    @abstractmethod
    def cinema_movie_create_validate(cls, body: any) -> ResponseWrapper:
        pass
