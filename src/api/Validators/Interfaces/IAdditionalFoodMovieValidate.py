from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class IAdditionalFoodMovieValidate(ABC):

    @abstractmethod
    def additional_food_create_validate(cls, body: any) -> ResponseWrapper:
        pass
