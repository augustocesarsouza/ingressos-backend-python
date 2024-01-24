from src.api.ControllersInterface.IAdditionalInfoUserController import IAdditionalInfoUserController
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.HttpTypes.HttpResponse import HttpResponse
from src.application.DTOs.AdditionalInfoUserDTO import AdditionalInfoUserDTO
from src.application.Services.Interfaces.IAdditionalInfoUserService import IAdditionalInfoUserService
from src.api.Validators.AdditionalInfoUserValidate import user_update_validate


class AdditionalInfoUserController(IAdditionalInfoUserController):
    def __init__(self, additional_info_user_service: IAdditionalInfoUserService) -> None:
        self.__additional_info_user_service = additional_info_user_service

    def get_info_user(self, http_request: HttpRequest) -> HttpResponse:
        id_guid = http_request.path_params["idGuid"]
        reponse = self.__additional_info_user_service.get_info_user(id_guid)

        if reponse.IsSuccess:
            return HttpResponse(
                status_code=200,
                body={"data": reponse.Data}
            )
        else:
            return HttpResponse(
                status_code=400,
                body={"data": reponse.Data}
            )

    def update_async(self, http_request: HttpRequest) -> HttpResponse:
        result = user_update_validate(http_request.body)

        if not result.IsSuccess:
            return HttpResponse(
                status_code=422,
                body={"data": result.Data}
            )

        password = http_request.path_params["password"]

        userId = http_request.body['userId']
        birthDateString = http_request.body['birthDateString']
        gender = http_request.body['gender']
        phone = http_request.body['phone']
        cep = http_request.body['cep']
        logradouro = http_request.body['logradouro']
        numero = http_request.body['numero']
        complemento = http_request.body['complemento']
        referencia = http_request.body['referencia']
        bairro = http_request.body['bairro']
        estado = http_request.body['estado']
        cidade = http_request.body['cidade']

        additional_info_user_DTO = AdditionalInfoUserDTO(
            None, userId, None, birthDateString, gender, phone, cep, logradouro, numero, complemento, referencia, bairro, estado, cidade)

        response = self.__additional_info_user_service.update_async(
            additional_info_user_DTO, password)

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
