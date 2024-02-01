from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class IRegionTheatreRepository(ABC):

    @abstractmethod
    def get_by_theatre_id(cls, theatre_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def delete(cls, region_theatre_id: str) -> ResponseWrapper:
        pass
