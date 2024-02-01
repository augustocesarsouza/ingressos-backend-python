from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class ICloudinaryUti(ABC):

    @abstractmethod
    def create_img(self, base_64: str, width: int, height: int) -> ResponseWrapper:
        pass

    @abstractmethod
    def delete_img(self, public_id: str) -> ResponseWrapper:
        pass
