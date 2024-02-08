from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.infradata.Maps.AdditionalFoodMovieMap import AdditionalFoodMovieMap


class IAdditionalFoodMovieRepository(ABC):

    @abstractmethod
    def get_all_food_movie(cls, movie_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_additional_food_movie_id_by_movie_id(cls, movie_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def create(cls, additional_food_movie_map: AdditionalFoodMovieMap) -> ResponseWrapper:
        pass

    @abstractmethod
    def delete(cls, additional_food_movie_id: str) -> ResponseWrapper:
        pass
