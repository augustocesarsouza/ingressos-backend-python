from abc import ABC, abstractmethod
from src.application.DTOs.AdditionalFoodMovieDTO import AdditionalFoodMovieDTO
from src.application.Services.ResponseWrapper import ResponseWrapper


class IAdditionalFoodMovieService(ABC):

    @abstractmethod
    def get_all_food_movie(cls, movie_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def create(cls, additional_food_movie_dto: AdditionalFoodMovieDTO) -> ResponseWrapper:
        pass

    @abstractmethod
    def delete_additional_food_movie_by_movie_id(self, movie_id: str) -> ResponseWrapper:
        pass
