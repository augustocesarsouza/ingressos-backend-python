from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class IMovieRegionTicketsPurchesedValidate(ABC):

    @abstractmethod
    def movie_region_create_validate(cls, body: any) -> ResponseWrapper:
        pass

    @abstractmethod
    def movie_region_update_validate(cls, body: any) -> ResponseWrapper:
        pass
