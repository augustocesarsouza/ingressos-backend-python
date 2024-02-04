from abc import ABC, abstractmethod
from src.application.DTOs.MovieRegionTicketsPurchesedDTO import MovieRegionTicketsPurchesedDTO
from src.application.Services.ResponseWrapper import ResponseWrapper


class IMovieRegionTicketsPurchesedService(ABC):

    @abstractmethod
    def get_by_movie_id_and_cinema_id(cls, movie_id: str, cinema_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def create(cls, movie_region_tickets_purchesed_dto: MovieRegionTicketsPurchesedDTO) -> ResponseWrapper:
        pass

    @abstractmethod
    def update(cls, movie_region_tickets_purchesed_dto: MovieRegionTicketsPurchesedDTO) -> ResponseWrapper:
        pass
