from src.application.DTOs.MovieTheaterDTO import MovieTheaterDTO
from src.application.Services.Interfaces.IMovieTheaterService import IMovieTheaterService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IMovieTheaterRepository import IMovieTheaterRepository


class MovieTheaterService(IMovieTheaterService):
    def __init__(self, movie_theater_repository: IMovieTheaterRepository) -> None:
        self.__movie_theater_repository = movie_theater_repository

    def get_by_id_movie(self, movie_id: str) -> ResponseWrapper:
        pass

    def delete(self, movie_id: str) -> ResponseWrapper:
        movie_theater = self.__movie_theater_repository.get_by_movie_id(
            movie_id)

        if not movie_theater.IsSuccess:
            return movie_theater

        if movie_theater.Data == None or len(movie_theater.Data) <= 0:
            return ResponseWrapper.fail("NOT FOULD result")

        movie_theater_all: list[MovieTheaterDTO] = movie_theater.Data

        if len(movie_theater_all) > 0:
            for el in movie_theater_all:
                result_delete_movie_theater = self.__movie_theater_repository.delete(
                    el['id'])

        if not result_delete_movie_theater.IsSuccess:
            return result_delete_movie_theater

        return result_delete_movie_theater
