from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class IRegionTheatreService(ABC):

    @abstractmethod
    def delete(cls, theatre_id: str) -> ResponseWrapper:
        pass
