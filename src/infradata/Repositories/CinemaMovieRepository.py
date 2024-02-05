from src.application.DTOs.CinemaDTO import CinemaDTO
from src.application.DTOs.CinemaMovieDTO import CinemaMovieDTO
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.ICinemaMovieRepository import ICinemaMovieRepository
from src.infradata.Context.ApplicationDbContext import ApplicationDbContext
from src.infradata.Maps.CinemaMap import CinemaMap
from src.infradata.Maps.CinemaMovieMap import CinemaMovieMap
from sqlalchemy.exc import SQLAlchemyError


class CinemaMovieRepository(ICinemaMovieRepository):

    @classmethod
    def get_by_region_cinema_id_and_movie_id(self, region_id: str, movie_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                cinema_movie = (  # testar esse GET
                    database.session
                    .query(CinemaMovieMap.ScreeningSchedule, CinemaMap.Id, CinemaMap.NameCinema, CinemaMap.District, CinemaMap.Ranking)
                    .filter(CinemaMovieMap.RegionId == region_id and CinemaMovieMap.MovieId == movie_id)
                    .first()
                )
                database.session.commit()

                if cinema_movie != None:
                    cinema_dto = CinemaDTO(
                        id=cinema_movie.Id, nameCinema=cinema_movie.NameCinema, district=cinema_movie.District, ranking=cinema_movie.Ranking).to_dict()

                    cinema_movie_DTO = CinemaMovieDTO(id=None, cinemaId=None, movieId=None, regionId=None,
                                                      screeningSchedule=cinema_movie.ScreeningSchedule,
                                                      cinemaDTO=cinema_dto).to_dict()

                    return ResponseWrapper.ok(cinema_movie_DTO)
                else:
                    return ResponseWrapper.ok(cinema_movie)

            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def get_all_cinema_movie_id_by_movie_id(cls, movie_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                list_form_of_payment = (
                    database.session
                    .query(CinemaMovieMap.Id)
                    .filter(CinemaMovieMap.MovieId == movie_id)
                    .all()
                )
                database.session.commit()

                if list_form_of_payment != None:
                    array = []
                    for el in list_form_of_payment:
                        cinema_movie_DTO = CinemaMovieDTO(id=el.Id, cinemaId=None, movieId=None, regionId=None,
                                                          screeningSchedule=None,
                                                          cinemaDTO=None).to_dict()

                        array.append(cinema_movie_DTO)

                    return ResponseWrapper.ok(array)
                else:
                    return ResponseWrapper.ok(list_form_of_payment)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def create(self, cinema_movie_map: CinemaMovieMap) -> ResponseWrapper:
        with ApplicationDbContext() as database:

            cinema_dto = CinemaMovieDTO(
                id=None, cinemaId=cinema_movie_map.CinemaId, movieId=cinema_movie_map.MovieId, regionId=None, screeningSchedule=None, cinemaDTO=None).to_dict()

        try:
            database.session.begin()
            database.session.add(cinema_movie_map)
            database.session.commit()
            return ResponseWrapper.ok(cinema_dto)
        except SQLAlchemyError as exception:
            database.session.rollback()
            exception_name = type(exception).__name__
            return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def delete(cls, cinema_movie_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:

            try:
                database.session.begin()

                delete_cinema_movie = database.session.query(CinemaMovieMap).filter(
                    CinemaMovieMap.Id == cinema_movie_id).first()

                database.session.delete(delete_cinema_movie)
                database.session.commit()

                cinema_movie_DTO = CinemaMovieDTO(id=delete_cinema_movie.Id, cinemaId=None, movieId=None, regionId=None,
                                                  screeningSchedule=None,
                                                  cinemaDTO=None).to_dict()

                return ResponseWrapper.ok(cinema_movie_DTO)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")
