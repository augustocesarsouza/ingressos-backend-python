from abc import ABC, abstractmethod

from src.application.Services.ResponseWrapper import ResponseWrapper


class IRegionService(ABC):

    @abstractmethod
    def get_region_id(self, state: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_id_by_name_city(self, state: str) -> ResponseWrapper:
        pass
