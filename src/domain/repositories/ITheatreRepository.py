from abc import ABC, abstractmethod
from src.application.DTOs.TheatreDTO import TheatreDTO
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.infradata.Maps.TheatreMap import TheatreMap


class ITheatreRepository(ABC):

    @abstractmethod
    def get_by_id(cls, theatre_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_by_id_only_publicId(cls, theatre_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_by_id_all_props(cls, theatre_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_all_theatre_by_region_id(cls, region_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def create(cls, theatre: TheatreMap) -> ResponseWrapper:
        pass

    @abstractmethod  # MovieRepository olha lá tem
    def delete(cls, id_theatre: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def update(cls, theatre_DTO: TheatreDTO) -> ResponseWrapper:
        pass
