from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class ITheatreValidate(ABC):

    @abstractmethod
    def theatre_create_validate(cls, body: any) -> ResponseWrapper:
        pass

    @abstractmethod
    def theatre_update_img_validate(cls, body: any) -> ResponseWrapper:
        pass
