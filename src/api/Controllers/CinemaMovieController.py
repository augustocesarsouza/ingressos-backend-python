from src.api.ControllersInterface.ICinemaMovieController import ICinemaMovieController
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.HttpTypes.HttpResponse import HttpResponse
from src.api.Validators.Interfaces.ICinemaMovieValidate import ICinemaMovieValidate
from src.application.DTOs.CinemaMovieDTO import CinemaMovieDTO
from src.application.Services.Interfaces.ICinemaMovieService import ICinemaMovieService


class CinemaMovieController(ICinemaMovieController):
    def __init__(self, cinema_movie_service: ICinemaMovieService, cinema_movie_validate: ICinemaMovieValidate) -> None:
        self.__cinema_movie_service = cinema_movie_service
        self.__cinema_movie_validate = cinema_movie_validate

    def get_by_region_cinema_id_and_movie_id(self, http_request: HttpRequest) -> HttpResponse:
        city_name = http_request.path_params["region"]
        movieId = http_request.path_params["movieId"]

        result_get_region = self.__cinema_movie_service.get_by_region_cinema_id_and_movie_id(
            city_name, movieId)

        if result_get_region.IsSuccess:
            return HttpResponse(
                status_code=200,
                body={"data": result_get_region.Data}
            )
        else:
            return HttpResponse(
                status_code=400,
                body={"data": result_get_region.Data}
            )

    def create(self, http_request: HttpRequest) -> HttpResponse:
        result_validate_body = self.__cinema_movie_validate.cinema_movie_create_validate(
            http_request.body)

        if not result_validate_body.IsSuccess:
            return HttpResponse(
                status_code=422,
                body={"data": result_validate_body.Data}
            )

        cinemaId = http_request.body["cinemaId"]
        movieId = http_request.body["movieId"]
        regionId = http_request.body["regionId"]
        screeningSchedule = http_request.body["screeningSchedule"]

        cinema_movie_dto = CinemaMovieDTO(
            id=None, cinemaId=cinemaId, movieId=movieId, regionId=regionId, screeningSchedule=screeningSchedule, cinemaDTO=None)

        result_create = self.__cinema_movie_service.create(cinema_movie_dto)

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
