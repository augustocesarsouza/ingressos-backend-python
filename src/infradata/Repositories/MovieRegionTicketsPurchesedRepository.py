from src.application.DTOs.MovieRegionTicketsPurchesedDTO import MovieRegionTicketsPurchesedDTO
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IMovieRegionTicketsPurchesedRepository import IMovieRegionTicketsPurchesedRepository
from src.infradata.Context.ApplicationDbContext import ApplicationDbContext
from src.infradata.Maps.MovieRegionTicketsPurchesedMap import MovieRegionTicketsPurchesedMap
from sqlalchemy.exc import SQLAlchemyError


class MovieRegionTicketsPurchesedRepository(IMovieRegionTicketsPurchesedRepository):

    @classmethod
    def get_list_register_by_movie_id(cls, movie_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                movie_region_tickets_purchesed_list = (
                    database.session
                    .query(MovieRegionTicketsPurchesedMap.Id)
                    .filter(MovieRegionTicketsPurchesedMap.MovieId == movie_id)
                    .all()
                )
                database.session.commit()

                if len(movie_region_tickets_purchesed_list) > 0:
                    list_movie_region_tickets_purchesed = []

                    for el in movie_region_tickets_purchesed_list:
                        movie_region_tickets_purchesed_DTO = MovieRegionTicketsPurchesedDTO(id=el.Id, ticketsSeats=None,
                                                                                            movieId=None, movieDTO=None, cinemaId=None, cinemaDTO=None)
                        list_movie_region_tickets_purchesed.append(
                            movie_region_tickets_purchesed_DTO)

                    return ResponseWrapper.ok(list_movie_region_tickets_purchesed)
                else:
                    return ResponseWrapper.ok(movie_region_tickets_purchesed_list)

            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def get_by_movie_id_and_cinema_id(cls, movie_id: str, cinema_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                movie_region_tickets_purchesed = (
                    database.session
                    .query(MovieRegionTicketsPurchesedMap.Id, MovieRegionTicketsPurchesedMap.TicketsSeats)
                    .filter(MovieRegionTicketsPurchesedMap.MovieId == movie_id and MovieRegionTicketsPurchesedMap.CinemaId == cinema_id)
                    .first()
                )
                database.session.commit()

                if movie_region_tickets_purchesed != None:
                    movie_region_tickets_purchesed_DTO = MovieRegionTicketsPurchesedDTO(
                        id=movie_region_tickets_purchesed.Id, ticketsSeats=movie_region_tickets_purchesed.TicketsSeats, movieId=None, movieDTO=None, cinemaId=None, cinemaDTO=None).to_dict()

                    return ResponseWrapper.ok(movie_region_tickets_purchesed_DTO)
                else:
                    return ResponseWrapper.ok(movie_region_tickets_purchesed)

            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def create(cls, movie_region_tickets_purchesed_map: MovieRegionTicketsPurchesedMap) -> ResponseWrapper:
        with ApplicationDbContext() as database:

            movie_region_tickets_purchesed_DTO = MovieRegionTicketsPurchesedDTO(
                id=None, ticketsSeats=movie_region_tickets_purchesed_map.TicketsSeats, movieId=movie_region_tickets_purchesed_map.MovieId, movieDTO=None, cinemaId=movie_region_tickets_purchesed_map.CinemaId, cinemaDTO=None).to_dict()

        try:
            database.session.begin()
            database.session.add(movie_region_tickets_purchesed_map)
            database.session.commit()
            return ResponseWrapper.ok(movie_region_tickets_purchesed_DTO)
        except SQLAlchemyError as exception:
            database.session.rollback()
            exception_name = type(exception).__name__
            return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def update(cls, movie_region_tickets_purchesed_dto: MovieRegionTicketsPurchesedDTO) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                movie_region_tickets_purchesed = database.session.query(MovieRegionTicketsPurchesedMap).filter(
                    MovieRegionTicketsPurchesedMap.Id == movie_region_tickets_purchesed_dto.Id).first()

                if movie_region_tickets_purchesed != None:
                    movie_region_tickets_purchesed.TicketsSeats = movie_region_tickets_purchesed_dto.TicketsSeats

                database.session.commit()
                return ResponseWrapper.ok(movie_region_tickets_purchesed_dto.to_dict())
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def delete(cls, movie_region_tickets_purchesed_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()

                movie_region_tickets_purchesed = database.session.query(
                    MovieRegionTicketsPurchesedMap).filter_by(Id=movie_region_tickets_purchesed_id).first()

                database.session.delete(movie_region_tickets_purchesed)
                database.session.commit()

                movie_region_tickets_purchesed_DTO = MovieRegionTicketsPurchesedDTO(
                    id=movie_region_tickets_purchesed.Id, ticketsSeats=movie_region_tickets_purchesed.TicketsSeats, movieId=None, movieDTO=None, cinemaId=None, cinemaDTO=None).to_dict()

                return ResponseWrapper.ok(movie_region_tickets_purchesed_DTO)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")
