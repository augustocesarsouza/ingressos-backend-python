import unittest
from unittest.mock import Mock
from src.application.DTOs.CinemaMovieDTO import CinemaMovieDTO
from src.application.Services.ResponseWrapper import ResponseWrapper

from src.application.Services.CinemaMovieService import CinemaMovieService
from src.application.Services.Interfaces.ICinemaService import ICinemaService
from src.application.Services.Interfaces.IMovieService import IMovieService
from src.application.Services.Interfaces.IRegionService import IRegionService
from src.domain.repositories.ICinemaMovieRepository import ICinemaMovieRepository


class Test_CinemaMovieService(unittest.TestCase):

    def setUp(self) -> None:
        self.mock_cinema_movie_repository = Mock(ICinemaMovieRepository)
        self.mock_region_service = Mock(IRegionService)
        self.mock_cinema_service = Mock(ICinemaService)
        self.mock_movie_service = Mock(IMovieService)

    # method test "get_by_region_cinema_id_and_movie_id"
    def test_get_by_region_cinema_id_and_movie_id_without_error(self):
        region_get = {"id": "b311b0fb-b975-4d4d-afac-7a6c40307ee5",
                      "state": None, "city": None}

        # region_DTO = RegionDTO(
        #                 id=region.Id, state=None, city=None).to_dict()

        self.mock_region_service.get_region_id_by_city_name.return_value = ResponseWrapper.ok(
            region_get)

        self.mock_cinema_movie_repository.get_by_region_cinema_id_and_movie_id.return_value = ResponseWrapper.ok(
            "Ok")

        movie_service = CinemaMovieService(
            self.mock_cinema_movie_repository, self.mock_region_service, self.mock_cinema_service, self.mock_movie_service)

        result = movie_service.get_by_region_cinema_id_and_movie_id(
            "Campinas", "2b41445e-b9a2-491d-9fe5-9f9d48cc6700")

        self.assertEqual(result.IsSuccess, True)

    def test_get_by_region_cinema_id_and_movie_id_error_get_region_id(self):
        self.mock_region_service.get_region_id_by_city_name.return_value = ResponseWrapper.fail(
            "error get region id")

        movie_service = CinemaMovieService(
            self.mock_cinema_movie_repository, self.mock_region_service, self.mock_cinema_service, self.mock_movie_service)

        result = movie_service.get_by_region_cinema_id_and_movie_id(
            "Campinas", "2b41445e-b9a2-491d-9fe5-9f9d48cc6700")

        self.assertEqual(result.IsSuccess, False)

    def test_get_by_region_cinema_id_and_movie_id_error_get_by_region_cinema_id(self):
        region_get = {"id": "b311b0fb-b975-4d4d-afac-7a6c40307ee5",
                      "state": None, "city": None}

        self.mock_region_service.get_region_id_by_city_name.return_value = ResponseWrapper.ok(
            region_get)

        self.mock_cinema_movie_repository.get_by_region_cinema_id_and_movie_id.return_value = ResponseWrapper.fail(
            "error get region movie")

        movie_service = CinemaMovieService(
            self.mock_cinema_movie_repository, self.mock_region_service, self.mock_cinema_service, self.mock_movie_service)

        result = movie_service.get_by_region_cinema_id_and_movie_id(
            "Campinas", "2b41445e-b9a2-491d-9fe5-9f9d48cc6700")

        self.assertEqual(result.IsSuccess, False)

    # method test "create"
    def test_create_without_error(self):
        self.mock_cinema_service.get_cinema_by_id_check_exist.return_value = ResponseWrapper.ok(
            "registry cinema there is")

        self.mock_region_service.get_region_by_id_check_exist.return_value = ResponseWrapper.ok(
            "registry region there is")

        self.mock_movie_service.get_movie_by_id_check_exist.return_value = ResponseWrapper.ok(
            "registry movie there is")

        self.mock_cinema_movie_repository.create.return_value = ResponseWrapper.ok(
            "created successfully")

        cinema_movie_dto = CinemaMovieDTO(None, "2b7f9169-99b3-4cb2-baaf-8429f2e0e4ca",
                                          "edf216ab-e7c8-4729-9754-fd6b536f853c", "820454e0-269a-4f21-b1f6-fe76bac3ea83", None, None)

        movie_service = CinemaMovieService(
            self.mock_cinema_movie_repository, self.mock_region_service, self.mock_cinema_service, self.mock_movie_service)

        result = movie_service.create(cinema_movie_dto)
        self.assertEqual(result.IsSuccess, True)

    def test_create_error_DTO_None(self):
        movie_service = CinemaMovieService(
            self.mock_cinema_movie_repository, self.mock_region_service, self.mock_cinema_service, self.mock_movie_service)

        result = movie_service.create(None)
        self.assertEqual(result.IsSuccess, False)

    def test_create_not_found_registry_cinema(self):
        self.mock_cinema_service.get_cinema_by_id_check_exist.return_value = ResponseWrapper.fail(
            "cinema registry not found")

        cinema_movie_dto = CinemaMovieDTO(None, "2b7f9169-99b3-4cb2-baaf-8429f2e0e4ca",
                                          "edf216ab-e7c8-4729-9754-fd6b536f853c", "820454e0-269a-4f21-b1f6-fe76bac3ea83", None, None)

        movie_service = CinemaMovieService(
            self.mock_cinema_movie_repository, self.mock_region_service, self.mock_cinema_service, self.mock_movie_service)

        result = movie_service.create(cinema_movie_dto)
        self.assertEqual(result.IsSuccess, False)

    def test_create_not_found_registry_region(self):
        self.mock_cinema_service.get_cinema_by_id_check_exist.return_value = ResponseWrapper.ok(
            "registry cinema there is")

        self.mock_region_service.get_region_by_id_check_exist.return_value = ResponseWrapper.fail(
            "region registry not found")

        cinema_movie_dto = CinemaMovieDTO(None, "2b7f9169-99b3-4cb2-baaf-8429f2e0e4ca",
                                          "edf216ab-e7c8-4729-9754-fd6b536f853c", "820454e0-269a-4f21-b1f6-fe76bac3ea83", None, None)

        movie_service = CinemaMovieService(
            self.mock_cinema_movie_repository, self.mock_region_service, self.mock_cinema_service, self.mock_movie_service)

        result = movie_service.create(cinema_movie_dto)
        self.assertEqual(result.IsSuccess, False)

    def test_create_not_found_registry_movie(self):
        self.mock_cinema_service.get_cinema_by_id_check_exist.return_value = ResponseWrapper.ok(
            "registry cinema there is")

        self.mock_region_service.get_region_by_id_check_exist.return_value = ResponseWrapper.ok(
            "registry region there is")

        self.mock_movie_service.get_movie_by_id_check_exist.return_value = ResponseWrapper.fail(
            "movie registry not found")

        cinema_movie_dto = CinemaMovieDTO(None, "2b7f9169-99b3-4cb2-baaf-8429f2e0e4ca",
                                          "edf216ab-e7c8-4729-9754-fd6b536f853c", "820454e0-269a-4f21-b1f6-fe76bac3ea83", None, None)

        movie_service = CinemaMovieService(
            self.mock_cinema_movie_repository, self.mock_region_service, self.mock_cinema_service, self.mock_movie_service)

        result = movie_service.create(cinema_movie_dto)
        self.assertEqual(result.IsSuccess, False)

    def test_create_error_when_create_cinema_movie(self):
        self.mock_cinema_service.get_cinema_by_id_check_exist.return_value = ResponseWrapper.ok(
            "registry cinema there is")

        self.mock_region_service.get_region_by_id_check_exist.return_value = ResponseWrapper.ok(
            "registry region there is")

        self.mock_movie_service.get_movie_by_id_check_exist.return_value = ResponseWrapper.ok(
            "registry movie there is")

        self.mock_cinema_movie_repository.create.return_value = ResponseWrapper.fail(
            "error when create cinema movie")

        cinema_movie_dto = CinemaMovieDTO(None, "2b7f9169-99b3-4cb2-baaf-8429f2e0e4ca",
                                          "edf216ab-e7c8-4729-9754-fd6b536f853c", "820454e0-269a-4f21-b1f6-fe76bac3ea83", None, None)

        movie_service = CinemaMovieService(
            self.mock_cinema_movie_repository, self.mock_region_service, self.mock_cinema_service, self.mock_movie_service)

        result = movie_service.create(cinema_movie_dto)
        self.assertEqual(result.IsSuccess, False)
