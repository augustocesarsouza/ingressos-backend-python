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

    def delete(self, movie_id: str) -> ResponseWrapper:
        if len(movie_id) < 36:
            return ResponseWrapper.fail("error movie_id provided must be greater than or equal to 36")

        result_get_list_register_by_movie_id = self.__movie_region_tickets_purchesed_repository.get_list_register_by_movie_id(
            movie_id)

        if not result_get_list_register_by_movie_id.IsSuccess:
            return result_get_list_register_by_movie_id

        movie_region_tickets_purchesed_list: list[
            MovieRegionTicketsPurchesedDTO] = result_get_list_register_by_movie_id.Data

        if len(movie_region_tickets_purchesed_list) <= 0:
            return ResponseWrapper.ok("not exist register with this movie_id")

        for el in movie_region_tickets_purchesed_list:
            result_delete_register_of_the_table = self.__movie_region_tickets_purchesed_repository.delete(
                el.Id)

            if not result_delete_register_of_the_table.IsSuccess:
                return ResponseWrapper.fail("error when delete register from movie_region_tickets_purchesed")

        return ResponseWrapper.ok("all deleted")
