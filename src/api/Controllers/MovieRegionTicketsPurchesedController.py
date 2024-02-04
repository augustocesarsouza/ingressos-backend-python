from src.api.ControllersInterface.IMovieRegionTicketsPurchesedController import IMovieRegionTicketsPurchesedController
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.HttpTypes.HttpResponse import HttpResponse
from src.api.Validators.Interfaces.IMovieRegionTicketsPurchesedValidate import IMovieRegionTicketsPurchesedValidate
from src.application.DTOs.MovieRegionTicketsPurchesedDTO import MovieRegionTicketsPurchesedDTO
from src.application.Services.Interfaces.IMovieRegionTicketsPurchesedService import IMovieRegionTicketsPurchesedService


class MovieRegionTicketsPurchesedController(IMovieRegionTicketsPurchesedController):
    def __init__(self, movie_region_tickets_purchesed_service: IMovieRegionTicketsPurchesedService, movie_region_tickets_purchesed_validate: IMovieRegionTicketsPurchesedValidate) -> None:
        self.__movie_region_tickets_purchesed_service = movie_region_tickets_purchesed_service
        self.__movie_region_tickets_purchesed_validate = movie_region_tickets_purchesed_validate

    def get_by_movie_id_and_cinema_id(self, http_request: HttpRequest) -> HttpResponse:
        movie_id = http_request.path_params["movieId"]
        cinema_id = http_request.path_params["cinemaId"]

        result_get_movie = self.__movie_region_tickets_purchesed_service.get_by_movie_id_and_cinema_id(
            movie_id, cinema_id)

        if result_get_movie.IsSuccess:
            return HttpResponse(
                status_code=200,
                body={"data": result_get_movie.Data}
            )
        else:
            return HttpResponse(
                status_code=400,
                body={"data": result_get_movie.Data}
            )

    def create(self, http_request: HttpRequest) -> HttpResponse:
        result_validate_body = self.__movie_region_tickets_purchesed_validate.movie_region_create_validate(
            http_request.body)

        if not result_validate_body.IsSuccess:
            return HttpResponse(
                status_code=422,
                body={"data": result_validate_body.Data}
            )

        movie_id = http_request.body["movieId"]
        cinema_id = http_request.body["cinemaId"]
        tickets_seats = http_request.body["ticketsSeats"]

        movie_region_tickets_purchesed_dto = MovieRegionTicketsPurchesedDTO(id=None, ticketsSeats=tickets_seats, movieId=movie_id,
                                                                            movieDTO=None, cinemaId=cinema_id, cinemaDTO=None)

        result_create = self.__movie_region_tickets_purchesed_service.create(
            movie_region_tickets_purchesed_dto)

        if result_create.IsSuccess:
            return HttpResponse(
                status_code=200,
                body={"data": result_create.Data}
            )
        else:
            return HttpResponse(
                status_code=400,
                body={"data": result_create.Data}
            )

    def update(self, http_request: HttpRequest) -> HttpResponse:
        result_validate_body_update = self.__movie_region_tickets_purchesed_validate.movie_region_create_validate(
            http_request.body)

        if not result_validate_body_update.IsSuccess:
            return HttpResponse(
                status_code=422,
                body={"data": result_validate_body_update.Data}
            )

        movie_id = http_request.body["movieId"]
        cinema_id = http_request.body["cinemaId"]
        tickets_seats = http_request.body["ticketsSeats"]

        movie_region_tickets_purchesed_dto = MovieRegionTicketsPurchesedDTO(id=None, ticketsSeats=tickets_seats, movieId=movie_id,
                                                                            movieDTO=None, cinemaId=cinema_id, cinemaDTO=None)

        result_update = self.__movie_region_tickets_purchesed_service.update(
            movie_region_tickets_purchesed_dto)

        if result_update.IsSuccess:
            return HttpResponse(
                status_code=200,
                body={"data": result_update.Data}
            )
        else:
            return HttpResponse(
                status_code=400,
                body={"data": result_update.Data}
            )
