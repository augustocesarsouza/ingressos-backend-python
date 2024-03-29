import uuid
from src.application.DTOs.CinemaMovieDTO import CinemaMovieDTO
from src.application.Services.Interfaces.ICinemaMovieService import ICinemaMovieService
from src.application.Services.Interfaces.ICinemaService import ICinemaService
from src.application.Services.Interfaces.IMovieService import IMovieService
from src.application.Services.Interfaces.IRegionService import IRegionService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.ICinemaMovieRepository import ICinemaMovieRepository
from src.infradata.Maps.CinemaMovieMap import CinemaMovieMap


class CinemaMovieService(ICinemaMovieService):
    def __init__(self, cinema_movie_repository: ICinemaMovieRepository, region_service: IRegionService, cinema_service: ICinemaService, movie_service: IMovieService) -> None:
        self.__cinema_movie_repository = cinema_movie_repository
        self.__region_service = region_service
        self.__cinema_service = cinema_service
        self.__movie_service = movie_service

    def get_by_region_cinema_id_and_movie_id(self, city_name: str, movie_id: str) -> ResponseWrapper:
        result_get_region = self.__region_service.get_region_id_by_city_name(
            city_name)

        if not result_get_region.IsSuccess:
            return result_get_region

        region = result_get_region.Data

        result_get_by_region_cinema_id = self.__cinema_movie_repository.get_by_region_cinema_id_and_movie_id(
            region["id"], movie_id)

        return result_get_by_region_cinema_id

    def create(self, cinema_movie_dto: CinemaMovieDTO) -> ResponseWrapper:
        if cinema_movie_dto == None:
            return ResponseWrapper.fail("DTO None")

        result_get_cinema_check_exist = self.__cinema_service.get_cinema_by_id_check_exist(
            cinema_movie_dto.CinemaId)

        if not result_get_cinema_check_exist.IsSuccess:
            return ResponseWrapper.fail("not exist cinema")

        result_get_region_check_exist = self.__region_service.get_region_by_id_check_exist(
            cinema_movie_dto.RegionId)

        if not result_get_region_check_exist.IsSuccess:
            return ResponseWrapper.fail("not exist region")

        result_get_movie_check_exist = self.__movie_service.get_movie_by_id_check_exist(
            cinema_movie_dto.MovieId)

        if not result_get_movie_check_exist.IsSuccess:
            return ResponseWrapper.fail("not exist movie")

        new_guid = uuid.uuid4()
        guid_str = str(new_guid)

        cinema_movie_map = CinemaMovieMap()
        cinema_movie_map.set_attributes(guid_str, cinema_movie_dto.CinemaId, cinema_movie_dto.MovieId,
                                        cinema_movie_dto.RegionId, cinema_movie_dto.ScreeningSchedule, None)

        result_create_cinema_movie = self.__cinema_movie_repository.create(
            cinema_movie_map)

        return result_create_cinema_movie

    def delete(self, movie_id: str) -> ResponseWrapper:
        if len(movie_id) < 36:
            return ResponseWrapper.fail("error movie_id provided must be greater than or equal to 36")

        result_get_list_cinema_movie_id = self.__cinema_movie_repository.get_all_cinema_movie_id_by_movie_id(
            movie_id)

        if not result_get_list_cinema_movie_id.IsSuccess:
            return result_get_list_cinema_movie_id

        list_cinema_movie_id: list[
            CinemaMovieDTO] = result_get_list_cinema_movie_id.Data

        if len(list_cinema_movie_id) <= 0:
            return ResponseWrapper.ok("not exist register with this movie_id")

        for el in list_cinema_movie_id:
            result_delete_register_of_the_table = self.__cinema_movie_repository.delete(
                el["id"])

            if not result_delete_register_of_the_table.IsSuccess:
                return ResponseWrapper.fail("error when delete register from movie_region_tickets_purchesed")

        return ResponseWrapper.ok("all deleted")
