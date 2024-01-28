from abc import ABC, abstractmethod

from src.application.Services.ResponseWrapper import ResponseWrapper


class IRegionRepository(ABC):

    @abstractmethod
    def get_region_id(cls, region: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_id_by_name_city(cls, state: str) -> ResponseWrapper:
        pass
