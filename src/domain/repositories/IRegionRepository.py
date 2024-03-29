from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class IRegionRepository(ABC):

    @abstractmethod
    def get_region_by_id_check_exist(cls, region_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_region_id_by_city_name(cls, city: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_id_by_name_state(cls, state: str) -> ResponseWrapper:
        pass
