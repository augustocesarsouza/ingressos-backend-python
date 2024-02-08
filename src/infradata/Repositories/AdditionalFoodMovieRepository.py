from src.application.DTOs.AdditionalFoodMovieDTO import AdditionalFoodMovieDTO
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IAdditionalFoodMovieRepository import IAdditionalFoodMovieRepository
from src.infradata.Context.ApplicationDbContext import ApplicationDbContext
from src.infradata.Maps.AdditionalFoodMovieMap import AdditionalFoodMovieMap
from sqlalchemy.exc import SQLAlchemyError


class AdditionalFoodMovieRepository(IAdditionalFoodMovieRepository):

    @classmethod
    def get_all_food_movie(cls, movie_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                list_additional_food_movie = (
                    database.session
                    .query(AdditionalFoodMovieMap.Title, AdditionalFoodMovieMap.Price, AdditionalFoodMovieMap.Fee, AdditionalFoodMovieMap.ImgUrl)
                    .filter(AdditionalFoodMovieMap.MovieId == movie_id)
                    .all()
                )
                database.session.commit()

                if list_additional_food_movie != None:
                    array = []
                    for el in list_additional_food_movie:
                        additional_food_movie_dto = AdditionalFoodMovieDTO(id=None, title=el.Title, price=el.Price,
                                                                           fee=el.Fee, imgUrl=el.ImgUrl, publicId=None, base64Img=None,
                                                                           movieId=None, movie=None).to_dict()
                        array.append(additional_food_movie_dto)

                    return ResponseWrapper.ok(array)
                else:
                    return ResponseWrapper.ok(list_additional_food_movie)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def get_additional_food_movie_id_by_movie_id(cls, movie_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                list_additional_food_movie = (
                    database.session
                    .query(AdditionalFoodMovieMap.Id, AdditionalFoodMovieMap.PublicId)
                    .filter(AdditionalFoodMovieMap.MovieId == movie_id)
                    .all()
                )
                database.session.commit()

                if list_additional_food_movie != None:
                    array = []
                    for el in list_additional_food_movie:
                        additional_food_movie_dto = AdditionalFoodMovieDTO(id=el.Id, title=None, price=None,
                                                                           fee=None, imgUrl=None, publicId=el.PublicId, base64Img=None,
                                                                           movieId=None, movie=None)
                        array.append(additional_food_movie_dto)

                    return ResponseWrapper.ok(array)
                else:
                    return ResponseWrapper.ok(list_additional_food_movie)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def create(cls, additional_food_movie_map: AdditionalFoodMovieMap) -> ResponseWrapper:
        with ApplicationDbContext() as database:

            additional_food_movie_dto = AdditionalFoodMovieDTO(id=None, title=additional_food_movie_map.Title, price=additional_food_movie_map.Price,
                                                               fee=additional_food_movie_map.Fee, imgUrl=additional_food_movie_map.ImgUrl, publicId=None,
                                                               base64Img=None, movieId=None, movie=None).to_dict()

        try:
            database.session.begin()
            database.session.add(additional_food_movie_map)
            database.session.commit()
            return ResponseWrapper.ok(additional_food_movie_dto)
        except SQLAlchemyError as exception:
            database.session.rollback()
            exception_name = type(exception).__name__
            return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def delete(cls, additional_food_movie_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()

                result_get = database.session.query(
                    AdditionalFoodMovieMap).filter(AdditionalFoodMovieMap.Id == additional_food_movie_id).first()

                database.session.delete(result_get)
                database.session.commit()

                additional_food_movie_dto = AdditionalFoodMovieDTO(id=None, title=result_get.Title, price=result_get.Price,
                                                                   fee=result_get.Fee, imgUrl=None, publicId=None,
                                                                   base64Img=None, movieId=None, movie=None).to_dict()

                return ResponseWrapper.ok(additional_food_movie_dto)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")
