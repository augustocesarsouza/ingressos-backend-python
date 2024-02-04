import unittest
from unittest.mock import Mock

from src.application.Services.MovieTheaterService import MovieTheaterService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IMovieTheaterRepository import IMovieTheaterRepository


class Test_MovieTheaterService(unittest.TestCase):
    def setUp(self) -> None:
        self.movie_theater_repository = Mock(spec=IMovieTheaterRepository)

    # test func 'delete'
    def test_delete_without_error(self):
        array = []
        obj = {
            "id": "4f128207-3ceb-41b5-8645-1acb4add21a8",
            "movieId": "6cefaafb-5ef2-46af-8b7f-65e7332d5ce9",
            "regionId": "4f128207-3ceb-41b5-8645-1acb4add21a8"
        }

        array.append(obj)

        self.movie_theater_repository.get_by_movie_id.return_value = ResponseWrapper.ok(
            array)

        self.movie_theater_repository.delete.return_value = ResponseWrapper.ok(
            array)

        movie_service = MovieTheaterService(self.movie_theater_repository)

        result = movie_service.delete("e92da0j8-0c10-24d1-88ab-b270c43183a0")
        self.assertEqual(result.IsSuccess, True)

    def test_delete_error_database(self):
        self.movie_theater_repository.get_by_movie_id.return_value = ResponseWrapper.fail(
            "error database")

        movie_service = MovieTheaterService(self.movie_theater_repository)

        result = movie_service.delete("e92da0j8-0c10-24d1-88ab-b270c43183a0")
        self.assertEqual(result.IsSuccess, False)

    def test_delete_error_not_exist_movietheater_join(self):
        array = []

        self.movie_theater_repository.get_by_movie_id.return_value = ResponseWrapper.ok(
            array)

        movie_service = MovieTheaterService(self.movie_theater_repository)

        result = movie_service.delete("e92da0j8-0c10-24d1-88ab-b270c43183a0")
        self.assertEqual(result.IsSuccess, True)
        self.assertEqual(result.Data, "NOT FOULD result")

    def test_delete_error_database_delete_movietheater(self):
        array = []
        obj = {
            "id": "4f128207-3ceb-41b5-8645-1acb4add21a8",
            "movieId": "6cefaafb-5ef2-46af-8b7f-65e7332d5ce9",
            "regionId": "4f128207-3ceb-41b5-8645-1acb4add21a8"
        }

        array.append(obj)

        self.movie_theater_repository.get_by_movie_id.return_value = ResponseWrapper.ok(
            array)

        self.movie_theater_repository.delete.return_value = ResponseWrapper.fail(
            "error when delete movie_theater")

        movie_service = MovieTheaterService(self.movie_theater_repository)

        result = movie_service.delete("e92da0j8-0c10-24d1-88ab-b270c43183a0")
        self.assertEqual(result.IsSuccess, False)
