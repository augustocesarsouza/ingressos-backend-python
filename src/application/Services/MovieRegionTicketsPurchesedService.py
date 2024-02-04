import uuid
from src.application.DTOs.MovieRegionTicketsPurchesedDTO import MovieRegionTicketsPurchesedDTO
from src.application.Services.Interfaces.IMovieRegionTicketsPurchesedService import IMovieRegionTicketsPurchesedService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IMovieRegionTicketsPurchesedRepository import IMovieRegionTicketsPurchesedRepository
from src.infradata.Maps.MovieRegionTicketsPurchesedMap import MovieRegionTicketsPurchesedMap


class MovieRegionTicketsPurchesedService(IMovieRegionTicketsPurchesedService):
    def __init__(self, movie_region_tickets_purchesed_repository: IMovieRegionTicketsPurchesedRepository) -> None:
        self.__movie_region_tickets_purchesed_repository = movie_region_tickets_purchesed_repository

    def get_by_movie_id_and_cinema_id(self, movie_id: str, cinema_id: str) -> ResponseWrapper:
        movie_region_result = self.__movie_region_tickets_purchesed_repository.get_by_movie_id_and_cinema_id(
            movie_id, cinema_id)

        return movie_region_result
     # criar lá no movieService 'MovieRegionTicketsPurchesed' tem que deletar a junção lá tbm

    def create(self, movie_region_tickets_purchesed_dto: MovieRegionTicketsPurchesedDTO) -> ResponseWrapper:
        if movie_region_tickets_purchesed_dto == None:
            return ResponseWrapper.fail("error DTO informed Null")

        result_get_movie_region = self.__movie_region_tickets_purchesed_repository.get_by_movie_id_and_cinema_id(
            movie_region_tickets_purchesed_dto.MovieId, movie_region_tickets_purchesed_dto.CinemaId)

        if not result_get_movie_region.IsSuccess:
            return result_get_movie_region

        if result_get_movie_region.Data != None:
            return ResponseWrapper.fail("this junction already exists")

        new_guid = uuid.uuid4()
        guid_str = str(new_guid)

        movie_region_tickets_purchesed_map = MovieRegionTicketsPurchesedMap(Id=guid_str, TicketsSeats=movie_region_tickets_purchesed_dto.TicketsSeats,
                                                                            MovieId=movie_region_tickets_purchesed_dto.MovieId, MovieDTO=None, CinemaId=movie_region_tickets_purchesed_dto.CinemaId, CinemaDTO=None)

        result_create_region_tickets = self.__movie_region_tickets_purchesed_repository.create(
            movie_region_tickets_purchesed_map)

        return result_create_region_tickets

    def update(self, movie_region_tickets_purchesed_dto: MovieRegionTicketsPurchesedDTO) -> ResponseWrapper:
        if movie_region_tickets_purchesed_dto == None:
            return ResponseWrapper.fail("error DTO informed Null")

        result_get_movie_region = self.__movie_region_tickets_purchesed_repository.get_by_movie_id_and_cinema_id(
            movie_region_tickets_purchesed_dto.MovieId, movie_region_tickets_purchesed_dto.CinemaId)

        if not result_get_movie_region.IsSuccess:
            return result_get_movie_region

        if result_get_movie_region.Data == None:
            return ResponseWrapper.fail("not found record")

        movie_region_tickets_data: MovieRegionTicketsPurchesedDTO = result_get_movie_region.Data

        movie_region_tickets_data.tickets_seats_value(
            movie_region_tickets_purchesed_dto.TicketsSeats, movie_region_tickets_data.TicketsSeats)

        result_update = self.__movie_region_tickets_purchesed_repository.update(
            movie_region_tickets_data)

        return result_update
