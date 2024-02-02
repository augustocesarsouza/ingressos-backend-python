from abc import ABC, abstractmethod

from src.application.Services.ResponseWrapper import ResponseWrapper


class IRegionService(ABC):

    @abstractmethod
    def get_region_by_id_check_exist(self, region_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_region_id_by_city_name(self, city: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_id_by_name_state(self, state: str) -> ResponseWrapper:
        pass
