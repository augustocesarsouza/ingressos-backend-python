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
    def get_movie_by_id_check_exist(self, movie_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                movie = (
                    database.session
                    .query(MovieMap.Id)
                    .filter(MovieMap.Id == movie_id)
                    .first()
                )

                database.session.commit()

                if movie != None:
                    movie_dto = MovieDTO(id=movie.Id, title=None, description=None, gender=None, duration=None, movieRating=None, imgUrl=None, publicId=None,
                                         imgUrlBackground=None, publicIdImgBackgound=None, statusMovie=None, base_64_img=None).to_dict()
                    return ResponseWrapper.ok(movie_dto)
                else:
                    return ResponseWrapper.ok(movie)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def get_by_id_only_publicId_PublicIdImgBackgound(cls, id_movie: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                user = (
                    database.session
                    .query(MovieMap.PublicId, MovieMap.PublicIdImgBackgound)
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
                movie: MovieMap = (
                    database.session
                    .query(MovieMap.Id, MovieMap.Title, MovieMap.Description, MovieMap.Gender, MovieMap.Duration, MovieMap.MovieRating, MovieMap.ImgUrl, MovieMap.ImgUrlBackground)
                    .filter(MovieMap.Id == id_movie)
                    .first()
                )
                database.session.commit()

                if movie != None:
                    movie_dto = MovieDTO(id=movie.Id, title=movie.Title, description=movie.Description, gender=movie.Gender, duration=movie.Duration, movieRating=movie.MovieRating, imgUrl=movie.ImgUrl, publicId=None,
                                         imgUrlBackground=movie.ImgUrlBackground, publicIdImgBackgound=None, statusMovie=None, base_64_img=None).to_dict()

                    return ResponseWrapper.ok(movie_dto)
                else:
                    return ResponseWrapper.ok(movie)
                # return ResponseWrapper.ok(user)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def get_status_movie(cls, status_movie: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                movie = (
                    database.session
                    .query(MovieMap.Id, MovieMap.Title, MovieMap.Description, MovieMap.Gender, MovieMap.Duration, MovieMap.MovieRating, MovieMap.ImgUrl, MovieMap.StatusMovie)
                    .filter(MovieMap.StatusMovie == status_movie)
                    .first()
                )
                database.session.commit()

                if movie != None:

                    movie_dto = MovieDTO(id=movie.Id, title=movie.Title, description=movie.Description, gender=movie.Gender, duration=movie.Duration,
                                         movieRating=movie.MovieRating, imgUrl=movie.ImgUrl, publicId=None, imgUrlBackground=None, publicIdImgBackgound=None,
                                         statusMovie=None, base_64_img=None).to_dict()

                    return ResponseWrapper.ok(movie_dto)
                else:
                    return ResponseWrapper.ok(movie)

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

                if theatres != None:
                    array = []

                    for item in theatres:
                        obj = {
                            "id": item.Id,
                            "title": item.Title,
                            "imgUrl": item.ImgUrl,
                            "movieRating": item.MovieRating
                        }
                        array.append(obj)

                    return ResponseWrapper.ok(array)
                else:
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
    def update_movie(cls, movie_DTO: MovieDTO) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                movie = database.session.query(MovieMap).filter(
                    MovieMap.Id == movie_DTO.Id).first()

                if movie != None:
                    movie.ImgUrl = movie_DTO.ImgUrl
                    movie.PublicId = movie_DTO.PublicId
                    movie.ImgUrlBackground = movie_DTO.ImgUrlBackground
                    movie.PublicIdImgBackgound = movie_DTO.PublicIdImgBackgound
                database.session.commit()
                return ResponseWrapper.ok(movie_DTO.to_dict())
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")
