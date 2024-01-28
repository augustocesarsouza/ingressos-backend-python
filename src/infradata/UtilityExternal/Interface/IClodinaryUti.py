from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class IClodinaryUti(ABC):

    @abstractmethod
    def create_img(self, base_64: str, width: int, height: int) -> ResponseWrapper:
        pass
