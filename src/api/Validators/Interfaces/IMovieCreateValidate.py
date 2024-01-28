from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class IMovieCreateValidate(ABC):

    @abstractmethod
    def movie_create_validate(cls, body: any) -> ResponseWrapper:
        pass
