from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class IMovieValidate(ABC):

    @abstractmethod
    def movie_create_validate(cls, body: any) -> ResponseWrapper:
        pass

    @abstractmethod
    def movie_update_validate(cls, body: any) -> ResponseWrapper:
        pass
