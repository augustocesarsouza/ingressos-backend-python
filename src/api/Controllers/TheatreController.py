from src.api.ControllersInterface.ITheatreController import ITheatreController
from src.api.Validators.Interfaces.ITheatreValidate import ITheatreValidate
from src.application.DTOs.TheatreDTO import TheatreDTO
from src.application.Services.Interfaces.ITheatreService import ITheatreService
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.HttpTypes.HttpResponse import HttpResponse


class TheatreController(ITheatreController):
    def __init__(self, theatre_service: ITheatreService, theatre_validate: ITheatreValidate) -> None:
        self.__theatre_service = theatre_service
        self.__theatre_validate = theatre_validate

    def get_all_theatre_by_state_name(self, http_request: HttpRequest) -> HttpResponse:
        state = http_request.path_params["state"]

        result_get_all_theatre = self.__theatre_service.get_all_theatre_by_state_name(
            state)

        if result_get_all_theatre.IsSuccess:
            return HttpResponse(
                status_code=200,
                body={"data": result_get_all_theatre.Data}
            )
        else:
            return HttpResponse(
                status_code=400,
                body={"data": result_get_all_theatre.Data}
            )

    def create(self, http_request: HttpRequest) -> HttpResponse:
        result_valid_body = self.__theatre_validate.theatre_create_validate(
            http_request.body)

        if not result_valid_body.IsSuccess:
            return HttpResponse(
                status_code=422,
                body={"data": result_valid_body.Data}
            )

        title = http_request.body["title"]
        description = http_request.body["description"]
        location = http_request.body["location"]
        typeOfAttraction = http_request.body["typeOfAttraction"]
        category = http_request.body['category']
        base64Img = http_request.body['base64Img']
        dataString = http_request.body['dataString']

        theatre_DTO = TheatreDTO(id=None, title=title, description=description, data=None, location=location, typeOfAttraction=typeOfAttraction,
                                 category=category, imgUrl=None, publicId=None, base_64_img=base64Img, dataString=dataString)

        response = self.__theatre_service.create(theatre_DTO)

        if response.IsSuccess:
            return HttpResponse(
                status_code=200,
                body={"data": response.Data}
            )
        else:
            return HttpResponse(
                status_code=400,
                body={"data": response.Data}
            )

    def delete(self, http_request: HttpRequest) -> HttpResponse:
        id_theatre = http_request.path_params["idTheatre"]

        result_delete = self.__theatre_service.delete(id_theatre)

        if result_delete.IsSuccess:
            return HttpResponse(
                status_code=200,
                body={"data": result_delete.Data}
            )
        else:
            return HttpResponse(
                status_code=400,
                body={"data": result_delete.Data}
            )

    def update(self, http_request: HttpRequest) -> HttpResponse:
        result_valid_body_update = self.__theatre_validate.theatre_update_img_validate(
            http_request.body)

        if not result_valid_body_update.IsSuccess:
            return HttpResponse(
                status_code=422,
                body={"data": result_valid_body_update.Data}
            )

        id = http_request.body["id"]
        base64Img = http_request.body["base64Img"]

        theatre_DTO = TheatreDTO(id=id, title=None, description=None, data=None, location=None, typeOfAttraction=None,
                                 category=None, imgUrl=None, publicId=None, base_64_img=base64Img, dataString=None)

        result_update = self.__theatre_service.update_theatre_img(theatre_DTO)

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
