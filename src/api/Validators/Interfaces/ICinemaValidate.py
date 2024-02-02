from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class ICinemaValidate(ABC):

    @abstractmethod
    def cinema_create_validate(cls, body: any) -> ResponseWrapper:
        pass
