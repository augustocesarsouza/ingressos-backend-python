from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class IRegionRepository(ABC):

    @abstractmethod
    def get_city_id(cls, city: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_id_by_name_state(cls, state: str) -> ResponseWrapper:
        pass
