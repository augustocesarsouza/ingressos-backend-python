from abc import ABC, abstractmethod

from src.application.DTOs.TheatreDTO import TheatreDTO
from src.application.Services.ResponseWrapper import ResponseWrapper


class ITheatreService(ABC):

    @abstractmethod
    def get_all_theatre_by_state_name(cls, state_name: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def create(cls, theatre_DTO: TheatreDTO) -> ResponseWrapper:
        pass

    @abstractmethod
    def delete(cls, theatre_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def update_theatre_img(cls, theatre_DTO: TheatreDTO) -> ResponseWrapper:
        pass
