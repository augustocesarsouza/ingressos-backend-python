from src.application.DTOs.MovieTheaterDTO import MovieTheaterDTO
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IMovieTheaterRepository import IMovieTheaterRepository
from src.infradata.Context.ApplicationDbContext import ApplicationDbContext
from sqlalchemy.exc import SQLAlchemyError

from src.infradata.Maps.MovieTheaterMap import MovieTheaterMap


class MovieTheaterRepository(IMovieTheaterRepository):

    def get_by_id(cls, movie_theater_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                user = (
                    database.session
                    .query(MovieTheaterMap)
                    .filter(MovieTheaterMap.Id == movie_theater_id)
                    .first()
                )
                database.session.commit()
                return ResponseWrapper.ok(user)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    def get_by_movie_id(cls, id_movie: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                user_all = (
                    database.session
                    .query(MovieTheaterMap)
                    .filter(MovieTheaterMap.MovieId == id_movie)
                    .all()
                )
                database.session.commit()

                array = []

                for item in user_all:
                    obj = {
                        "id": item.Id,
                        "movieId": item.MovieId,
                        "regionId": item.RegionId
                    }
                    array.append(obj)

                return ResponseWrapper.ok(array)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    def delete(cls, movie_theater_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()

                movie_theater_delete = database.session.query(
                    MovieTheaterMap).filter_by(Id=movie_theater_id).first()

                database.session.delete(movie_theater_delete)
                database.session.commit()

                movie_theater_delete_DTO = MovieTheaterDTO(
                    movie_theater_delete.Id, movie_theater_delete.MovieId, movie_theater_delete.RegionId).to_dict()

                return ResponseWrapper.ok(movie_theater_delete_DTO)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")
