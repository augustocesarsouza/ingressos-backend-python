from src.api.ControllersInterface.ICinemaController import ICinemaController
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.HttpTypes.HttpResponse import HttpResponse
from src.api.Validators.Interfaces.ICinemaValidate import ICinemaValidate
from src.application.DTOs.CinemaDTO import CinemaDTO
from src.application.Services.Interfaces.ICinemaService import ICinemaService


class CinemaController(ICinemaController):
    def __init__(self, cinema_service: ICinemaService, cinema_validate: ICinemaValidate) -> None:
        self.__cinema_service = cinema_service
        self.__cinema_validate = cinema_validate

    def create(self, http_request: HttpRequest) -> HttpResponse:
        result_validate_body = self.__cinema_validate.cinema_create_validate(
            http_request.body)

        if not result_validate_body.IsSuccess:
            return HttpResponse(
                status_code=422,
                body={"data": result_validate_body.Data}
            )

        nameCinema = http_request.body["nameCinema"]
        district = http_request.body["district"]
        ranking = http_request.body["ranking"]

        cinema_dto = CinemaDTO(None, nameCinema=nameCinema,
                               district=district, ranking=ranking)

        result_create_cinema = self.__cinema_service.create(cinema_dto)

        if result_create_cinema.IsSuccess:
            return HttpResponse(
                status_code=200,
                body={"data": result_create_cinema.Data}
            )
        else:
            return HttpResponse(
                status_code=400,
                body={"data": result_create_cinema.Data}
            )
