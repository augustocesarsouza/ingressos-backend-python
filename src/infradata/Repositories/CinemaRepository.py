from src.application.DTOs.CinemaDTO import CinemaDTO
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.ICinemaRepository import ICinemaRepository
from src.infradata.Context.ApplicationDbContext import ApplicationDbContext
from src.infradata.Maps.CinemaMap import CinemaMap
from sqlalchemy.exc import SQLAlchemyError


class CinemaRepository(ICinemaRepository):

    @classmethod
    def get_cinema_by_id_check_exist(self, cinema_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                cinema = (
                    database.session
                    .query(CinemaMap.Id)
                    .filter(CinemaMap.Id == cinema_id)
                    .first()
                )
                database.session.commit()

                if cinema != None:
                    cinema_dto = CinemaDTO(
                        id=cinema.Id, nameCinema=None, district=None, ranking=None).to_dict()
                    return ResponseWrapper.ok(cinema_dto)
                else:
                    return ResponseWrapper.ok(cinema)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def create(self, cinema_map: CinemaMap) -> ResponseWrapper:
        with ApplicationDbContext() as database:

            cinema_dto = CinemaDTO(
                id=None, nameCinema=cinema_map.NameCinema, district=cinema_map.District, ranking=None).to_dict()

        try:
            database.session.begin()
            database.session.add(cinema_map)
            database.session.commit()
            return ResponseWrapper.ok(cinema_dto)
        except SQLAlchemyError as exception:
            database.session.rollback()
            exception_name = type(exception).__name__
            return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")
