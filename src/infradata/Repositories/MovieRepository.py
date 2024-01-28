from src.application.DTOs.MovieDTO import MovieDTO
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IMovieRepository import IMovieRepository
from src.infradata.Context.ApplicationDbContext import ApplicationDbContext
from src.infradata.Maps.MovieMap import MovieMap
from sqlalchemy.exc import SQLAlchemyError

from src.infradata.Maps.MovieTheaterMap import MovieTheaterMap


class MovieRepository(IMovieRepository):

    @classmethod
    def get_by_id(cls, id_movie: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                user = (
                    database.session
                    .query(MovieMap.Id, MovieMap.Title)
                    .filter(MovieMap.Id == id_movie)
                    .first()
                )
                database.session.commit()
                return ResponseWrapper.ok(user)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def get_info_movies_by_id(cls, id_movie: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                user: MovieMap = (
                    database.session
                    .query(MovieMap.Id, MovieMap.Title, MovieMap.Description, MovieMap.Gender, MovieMap.Duration, MovieMap.MovieRating, MovieMap.ImgUrl, MovieMap.ImgUrlBackground)
                    .filter(MovieMap.Id == id_movie)
                    .first()
                )
                database.session.commit()
                return ResponseWrapper.ok(user)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def get_status_movie(cls, status_movie: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                user = (
                    database.session
                    .query(MovieMap.Id, MovieMap.Title, MovieMap.Description, MovieMap.Gender, MovieMap.Duration, MovieMap.MovieRating, MovieMap.ImgUrl, MovieMap.StatusMovie)
                    .filter(MovieMap.StatusMovie == status_movie)
                    .first()
                )
                database.session.commit()
                return ResponseWrapper.ok(user)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def get_by_id_all_props(cls, id_movie: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                user = (
                    database.session
                    .query(MovieMap)
                    .filter(MovieMap.Id == id_movie)
                    .first()
                )
                database.session.commit()
                return ResponseWrapper.ok(user)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def get_all_movie_by_region_id(cls, region_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                theatres = (
                    database.session
                    .query(MovieMap)
                    .join(MovieTheaterMap, MovieMap.Id == MovieTheaterMap.MovieId)
                    .filter(MovieTheaterMap.RegionId == region_id)
                    .with_entities(
                        MovieMap.Id, MovieMap.Title, MovieMap.ImgUrl, MovieMap.MovieRating
                    ).all()
                )
                # já funciona estou pegando a lista de filme de cada região já
                database.session.commit()
                print(theatres)
                return ResponseWrapper.ok(theatres)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def create(cls, movie: MovieMap) -> ResponseWrapper:
        with ApplicationDbContext() as database:

            movie_DTO = MovieDTO(movie.Id, movie.Title, None, None, None, None,
                                 movie.ImgUrl, None, movie.ImgUrlBackground, None, None, None).to_dict()

            try:
                database.session.begin()
                database.session.add(movie)
                database.session.commit()
                return ResponseWrapper.ok(movie_DTO)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def delete(cls, id_movie: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()

                movie = database.session.query(
                    MovieMap).filter_by(Id=id_movie).first()

                database.session.delete(movie)
                database.session.commit()

                movie_delete_DTO = MovieDTO(movie.Id, movie.Title, None, None, None, None,
                                            None, movie.PublicId, None, movie.PublicIdImgBackgound, None, None).to_dict()

                return ResponseWrapper.ok(movie_delete_DTO)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    # olhar AdditionalInfoUserRepository, como foi feito
    def update_movie(cls, movie_DTO: MovieDTO) -> ResponseWrapper:
        pass
