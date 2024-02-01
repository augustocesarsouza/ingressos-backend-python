from abc import ABC, abstractmethod

from src.application.Services.ResponseWrapper import ResponseWrapper


class IRegionService(ABC):

    @abstractmethod
    def get_city_id(self, city: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_id_by_name_state(self, state: str) -> ResponseWrapper:
        pass
