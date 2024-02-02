import uuid
from src.application.DTOs.CinemaDTO import CinemaDTO
from src.application.Services.Interfaces.ICinemaService import ICinemaService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.ICinemaRepository import ICinemaRepository
from src.infradata.Maps.CinemaMap import CinemaMap


class CinemaService(ICinemaService):
    def __init__(self, cinema_repository: ICinemaRepository) -> None:
        self.__cinema_repository = cinema_repository

    def get_cinema_by_id_check_exist(self, cinema_id: str) -> ResponseWrapper:
        result_get = self.__cinema_repository.get_cinema_by_id_check_exist(
            cinema_id)

        if result_get.Data == None:
            return ResponseWrapper.fail("not fould movie")

        if not result_get.IsSuccess:
            return result_get

        return result_get

    def create(self, cinema_dto: CinemaDTO) -> ResponseWrapper:
        if cinema_dto == None:
            return ResponseWrapper.fail("error DTO None")

        new_guid = uuid.uuid4()
        guid_str = str(new_guid)

        cinema_map = CinemaMap()
        cinema_map.set_attributes(
            guid_str, cinema_dto.NameCinema, cinema_dto.District, cinema_dto.Ranking)

        result_create_cinema = self.__cinema_repository.create(cinema_map)

        return result_create_cinema
