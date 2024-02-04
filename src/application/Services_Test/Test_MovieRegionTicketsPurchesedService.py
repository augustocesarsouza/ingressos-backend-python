import unittest
from unittest.mock import Mock
from src.application.DTOs.MovieRegionTicketsPurchesedDTO import MovieRegionTicketsPurchesedDTO

from src.application.Services.MovieRegionTicketsPurchesedService import MovieRegionTicketsPurchesedService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IMovieRegionTicketsPurchesedRepository import IMovieRegionTicketsPurchesedRepository


class Test_MovieRegionTicketsPurchesedService(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_movie_region_tickets_purchesed_repository = Mock(
            spec=IMovieRegionTicketsPurchesedRepository)

    # test func 'get_by_movie_id_and_cinema_id'
    def test_get_by_movie_id_and_cinema_id_without_error(self):
        self.mock_movie_region_tickets_purchesed_repository.get_by_movie_id_and_cinema_id.return_value = ResponseWrapper.ok(
            "ok")

        movie_service = MovieRegionTicketsPurchesedService(
            self.mock_movie_region_tickets_purchesed_repository)

        result = movie_service.get_by_movie_id_and_cinema_id(
            "700b5f53-da49-419a-a514-59d4cc02e351", "a07811b6-8492-474a-8f4e-e910832c0128")
        self.assertEqual(result.IsSuccess, True)

    def test_get_by_movie_id_and_cinema_id_with_error(self):
        self.mock_movie_region_tickets_purchesed_repository.get_by_movie_id_and_cinema_id.return_value = ResponseWrapper.fail(
            "error")

        movie_service = MovieRegionTicketsPurchesedService(
            self.mock_movie_region_tickets_purchesed_repository)

        result = movie_service.get_by_movie_id_and_cinema_id(
            "700b5f53-da49-419a-a514-59d4cc02e351", "a07811b6-8492-474a-8f4e-e910832c0128")
        self.assertEqual(result.IsSuccess, False)

    # test func 'create'
    def test_create_without_error(self):
        self.mock_movie_region_tickets_purchesed_repository.get_by_movie_id_and_cinema_id.return_value = ResponseWrapper.ok(
            None)

        self.mock_movie_region_tickets_purchesed_repository.create.return_value = ResponseWrapper.ok(
            "created successfully")

        movie_region_tickets_purchesed_dto = MovieRegionTicketsPurchesedDTO(id=None, ticketsSeats="A1",
                                                                            movieId="700b5f53-da49-419a-a514-59d4cc02e351", movieDTO=None,
                                                                            cinemaId="a07811b6-8492-474a-8f4e-e910832c0128", cinemaDTO=None)

        movie_service = MovieRegionTicketsPurchesedService(
            self.mock_movie_region_tickets_purchesed_repository)

        result = movie_service.create(movie_region_tickets_purchesed_dto)
        self.assertEqual(result.IsSuccess, True)

    def test_create_with_error_dto_null(self):
        movie_service = MovieRegionTicketsPurchesedService(
            self.mock_movie_region_tickets_purchesed_repository)

        result = movie_service.create(None)
        self.assertEqual(result.IsSuccess, False)
        self.assertEqual(result.Data["message"], "error DTO informed Null")

    def test_create_with_error_get_by_movie_id_and_cinema_id_database_error(self):
        self.mock_movie_region_tickets_purchesed_repository.get_by_movie_id_and_cinema_id.return_value = ResponseWrapper.fail(
            "error datebase")

        movie_region_tickets_purchesed_dto = MovieRegionTicketsPurchesedDTO(id=None, ticketsSeats="A1",
                                                                            movieId="700b5f53-da49-419a-a514-59d4cc02e351", movieDTO=None,
                                                                            cinemaId="a07811b6-8492-474a-8f4e-e910832c0128", cinemaDTO=None)

        movie_service = MovieRegionTicketsPurchesedService(
            self.mock_movie_region_tickets_purchesed_repository)

        result = movie_service.create(movie_region_tickets_purchesed_dto)
        self.assertEqual(result.IsSuccess, False)

    def test_create_with_error_get_by_movie_id_and_cinema_id_already_exists_junction(self):
        self.mock_movie_region_tickets_purchesed_repository.get_by_movie_id_and_cinema_id.return_value = ResponseWrapper.ok(
            {})

        movie_region_tickets_purchesed_dto = MovieRegionTicketsPurchesedDTO(id=None, ticketsSeats="A1",
                                                                            movieId="700b5f53-da49-419a-a514-59d4cc02e351", movieDTO=None,
                                                                            cinemaId="a07811b6-8492-474a-8f4e-e910832c0128", cinemaDTO=None)

        movie_service = MovieRegionTicketsPurchesedService(
            self.mock_movie_region_tickets_purchesed_repository)

        result = movie_service.create(movie_region_tickets_purchesed_dto)
        self.assertEqual(result.IsSuccess, False)
        self.assertEqual(result.Data["message"],
                         "this junction already exists")

    def test_create_with_error_create_repository(self):
        self.mock_movie_region_tickets_purchesed_repository.get_by_movie_id_and_cinema_id.return_value = ResponseWrapper.ok(
            None)

        self.mock_movie_region_tickets_purchesed_repository.create.return_value = ResponseWrapper.fail(
            "error create repository")

        movie_region_tickets_purchesed_dto = MovieRegionTicketsPurchesedDTO(id=None, ticketsSeats="A1",
                                                                            movieId="700b5f53-da49-419a-a514-59d4cc02e351", movieDTO=None,
                                                                            cinemaId="a07811b6-8492-474a-8f4e-e910832c0128", cinemaDTO=None)

        movie_service = MovieRegionTicketsPurchesedService(
            self.mock_movie_region_tickets_purchesed_repository)

        result = movie_service.create(movie_region_tickets_purchesed_dto)
        self.assertEqual(result.IsSuccess, False)

    # test func 'update'
    def test_update_without_error(self):
        movie_region_tickets_purchesed_dto_database = MovieRegionTicketsPurchesedDTO(id=None, ticketsSeats="A1",
                                                                                     movieId=None, movieDTO=None,
                                                                                     cinemaId=None, cinemaDTO=None)

        self.mock_movie_region_tickets_purchesed_repository.get_by_movie_id_and_cinema_id.return_value = ResponseWrapper.ok(
            movie_region_tickets_purchesed_dto_database)

        self.mock_movie_region_tickets_purchesed_repository.update.return_value = ResponseWrapper.ok(
            "updated successfully")

        movie_region_tickets_purchesed_dto = MovieRegionTicketsPurchesedDTO(id=None, ticketsSeats="A2",
                                                                            movieId="700b5f53-da49-419a-a514-59d4cc02e351", movieDTO=None,
                                                                            cinemaId="a07811b6-8492-474a-8f4e-e910832c0128", cinemaDTO=None)

        movie_service = MovieRegionTicketsPurchesedService(
            self.mock_movie_region_tickets_purchesed_repository)

        result = movie_service.update(movie_region_tickets_purchesed_dto)
        self.assertEqual(result.IsSuccess, True)

    def test_update_with_error_dto_none(self):
        movie_service = MovieRegionTicketsPurchesedService(
            self.mock_movie_region_tickets_purchesed_repository)

        result = movie_service.update(None)
        self.assertEqual(result.IsSuccess, False)
        self.assertEqual(result.Data["message"], "error DTO informed Null")

    def test_update_with_error_get_by_movie_id_and_cinema_id_database_error(self):
        self.mock_movie_region_tickets_purchesed_repository.get_by_movie_id_and_cinema_id.return_value = ResponseWrapper.fail(
            "error database")

        movie_region_tickets_purchesed_dto = MovieRegionTicketsPurchesedDTO(id=None, ticketsSeats="A2",
                                                                            movieId="700b5f53-da49-419a-a514-59d4cc02e351", movieDTO=None,
                                                                            cinemaId="a07811b6-8492-474a-8f4e-e910832c0128", cinemaDTO=None)

        movie_service = MovieRegionTicketsPurchesedService(
            self.mock_movie_region_tickets_purchesed_repository)

        result = movie_service.update(movie_region_tickets_purchesed_dto)
        self.assertEqual(result.IsSuccess, False)

    def test_update_with_error_get_by_movie_id_and_cinema_id_error_not_found(self):
        self.mock_movie_region_tickets_purchesed_repository.get_by_movie_id_and_cinema_id.return_value = ResponseWrapper.ok(
            None)

        movie_region_tickets_purchesed_dto = MovieRegionTicketsPurchesedDTO(id=None, ticketsSeats="A2",
                                                                            movieId="700b5f53-da49-419a-a514-59d4cc02e351", movieDTO=None,
                                                                            cinemaId="a07811b6-8492-474a-8f4e-e910832c0128", cinemaDTO=None)

        movie_service = MovieRegionTicketsPurchesedService(
            self.mock_movie_region_tickets_purchesed_repository)

        result = movie_service.update(movie_region_tickets_purchesed_dto)
        self.assertEqual(result.IsSuccess, False)
        self.assertEqual(result.Data["message"], "not found record")

    def test_update_with_error_update_repository(self):
        movie_region_tickets_purchesed_dto_database = MovieRegionTicketsPurchesedDTO(id=None, ticketsSeats="A1",
                                                                                     movieId=None, movieDTO=None,
                                                                                     cinemaId=None, cinemaDTO=None)

        self.mock_movie_region_tickets_purchesed_repository.get_by_movie_id_and_cinema_id.return_value = ResponseWrapper.ok(
            movie_region_tickets_purchesed_dto_database)

        self.mock_movie_region_tickets_purchesed_repository.update.return_value = ResponseWrapper.fail(
            "error update repository")

        movie_region_tickets_purchesed_dto = MovieRegionTicketsPurchesedDTO(id=None, ticketsSeats="A2",
                                                                            movieId="700b5f53-da49-419a-a514-59d4cc02e351", movieDTO=None,
                                                                            cinemaId="a07811b6-8492-474a-8f4e-e910832c0128", cinemaDTO=None)

        movie_service = MovieRegionTicketsPurchesedService(
            self.mock_movie_region_tickets_purchesed_repository)

        result = movie_service.update(movie_region_tickets_purchesed_dto)
        self.assertEqual(result.IsSuccess, False)

    # test func 'delete'
    def test_delete_without_error(self):
        movie_region_tickets_purchesed_dto1 = MovieRegionTicketsPurchesedDTO(id="b7896127-76b1-48fb-bc64-9d6ab5d7da7f", ticketsSeats=None,
                                                                             movieId=None, movieDTO=None,
                                                                             cinemaId=None, cinemaDTO=None)

        movie_region_tickets_purchesed_dto2 = MovieRegionTicketsPurchesedDTO(id="beb929b7-1edb-404f-88ea-96ab9d949d9b", ticketsSeats=None,
                                                                             movieId=None, movieDTO=None,
                                                                             cinemaId=None, cinemaDTO=None)

        list_movie_region_tickets_purchesed = []
        list_movie_region_tickets_purchesed.append(
            movie_region_tickets_purchesed_dto1)
        list_movie_region_tickets_purchesed.append(
            movie_region_tickets_purchesed_dto2)

        self.mock_movie_region_tickets_purchesed_repository.get_list_register_by_movie_id.return_value = ResponseWrapper.ok(
            list_movie_region_tickets_purchesed)

        self.mock_movie_region_tickets_purchesed_repository.delete.side_effect = [
            ResponseWrapper.ok("deleted successfully1"),
            ResponseWrapper.ok("deleted successfully2")
        ]

        movie_service = MovieRegionTicketsPurchesedService(
            self.mock_movie_region_tickets_purchesed_repository)

        result = movie_service.delete("b46c262a-d45d-41e6-aed0-2a4649563fa2")
        self.assertEqual(result.IsSuccess, True)
        self.assertEqual(result.Data, "all deleted")

    def test_delete_with_error_movie_id_less_than_36(self):
        movie_service = MovieRegionTicketsPurchesedService(
            self.mock_movie_region_tickets_purchesed_repository)

        result = movie_service.delete("b46c262a-d45d-41e6-aed0-2a4649563fa")
        self.assertEqual(result.IsSuccess, False)
        self.assertEqual(
            result.Data["message"], "error movie_id provided must be greater than or equal to 36")

    def test_delete_with_error_get_list_registers_movie_region_tickets_purchesed_database_error(self):
        self.mock_movie_region_tickets_purchesed_repository.get_list_register_by_movie_id.return_value = ResponseWrapper.fail(
            "error database")

        movie_service = MovieRegionTicketsPurchesedService(
            self.mock_movie_region_tickets_purchesed_repository)

        result = movie_service.delete("b46c262a-d45d-41e6-aed0-2a4649563fa2")
        self.assertEqual(result.IsSuccess, False)

    def test_delete_with_error_list_empty(self):
        list_movie_region_tickets_purchesed = []

        self.mock_movie_region_tickets_purchesed_repository.get_list_register_by_movie_id.return_value = ResponseWrapper.ok(
            list_movie_region_tickets_purchesed)

        movie_service = MovieRegionTicketsPurchesedService(
            self.mock_movie_region_tickets_purchesed_repository)

        result = movie_service.delete("b46c262a-d45d-41e6-aed0-2a4649563fa2")
        self.assertEqual(result.IsSuccess, True)
        self.assertEqual(result.Data, "not exist register with this movie_id")

    def test_delete_with_error_delete_tickets_purchesed_list_first_element_ofthe_list(self):
        movie_region_tickets_purchesed_dto1 = MovieRegionTicketsPurchesedDTO(id="b7896127-76b1-48fb-bc64-9d6ab5d7da7f", ticketsSeats=None,
                                                                             movieId=None, movieDTO=None,
                                                                             cinemaId=None, cinemaDTO=None)

        movie_region_tickets_purchesed_dto2 = MovieRegionTicketsPurchesedDTO(id="beb929b7-1edb-404f-88ea-96ab9d949d9b", ticketsSeats=None,
                                                                             movieId=None, movieDTO=None,
                                                                             cinemaId=None, cinemaDTO=None)

        list_movie_region_tickets_purchesed = []

        list_movie_region_tickets_purchesed.append(
            movie_region_tickets_purchesed_dto1)
        list_movie_region_tickets_purchesed.append(
            movie_region_tickets_purchesed_dto2)

        self.mock_movie_region_tickets_purchesed_repository.get_list_register_by_movie_id.return_value = ResponseWrapper.ok(
            list_movie_region_tickets_purchesed)

        self.mock_movie_region_tickets_purchesed_repository.delete.return_value = ResponseWrapper.fail(
            "fail when delete")

        movie_service = MovieRegionTicketsPurchesedService(
            self.mock_movie_region_tickets_purchesed_repository)

        result = movie_service.delete("b46c262a-d45d-41e6-aed0-2a4649563fa2")
        self.assertEqual(result.IsSuccess, False)
        self.assertEqual(
            result.Data["message"], "error when delete register from movie_region_tickets_purchesed")

    def test_delete_with_error_delete_tickets_purchesed_list_second_element_ofthe_list(self):
        movie_region_tickets_purchesed_dto1 = MovieRegionTicketsPurchesedDTO(id="b7896127-76b1-48fb-bc64-9d6ab5d7da7f", ticketsSeats=None,
                                                                             movieId=None, movieDTO=None,
                                                                             cinemaId=None, cinemaDTO=None)

        movie_region_tickets_purchesed_dto2 = MovieRegionTicketsPurchesedDTO(id="beb929b7-1edb-404f-88ea-96ab9d949d9b", ticketsSeats=None,
                                                                             movieId=None, movieDTO=None,
                                                                             cinemaId=None, cinemaDTO=None)

        list_movie_region_tickets_purchesed = []
        list_movie_region_tickets_purchesed.append(
            movie_region_tickets_purchesed_dto1)
        list_movie_region_tickets_purchesed.append(
            movie_region_tickets_purchesed_dto2)

        self.mock_movie_region_tickets_purchesed_repository.get_list_register_by_movie_id.return_value = ResponseWrapper.ok(
            list_movie_region_tickets_purchesed)

        self.mock_movie_region_tickets_purchesed_repository.delete.side_effect = [
            ResponseWrapper.ok("deleted successfully1"),
            ResponseWrapper.fail("fail when delete")
        ]

        movie_service = MovieRegionTicketsPurchesedService(
            self.mock_movie_region_tickets_purchesed_repository)

        result = movie_service.delete("b46c262a-d45d-41e6-aed0-2a4649563fa2")
        self.assertEqual(result.IsSuccess, False)
        self.assertEqual(
            result.Data["message"], "error when delete register from movie_region_tickets_purchesed")
