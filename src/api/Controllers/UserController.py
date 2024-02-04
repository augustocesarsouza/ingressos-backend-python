from src.api.ControllersInterface.IUserController import IUserController
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.HttpTypes.HttpResponse import HttpResponse
from src.api.Validators.Interfaces.IUserCreateValidate import IUserCreateValidate
from src.application.DTOs.AdditionalInfoUserDTO import AdditionalInfoUserDTO
from src.application.DTOs.UserDTO import UserDTO
from src.application.Services.Interfaces.IUserConfirmationService import IUserConfirmationService
from src.application.Services.Interfaces.IUserManagementService import IUserManagementService
from src.application.Services.Interfaces.IUserAuthenticationService import IUserAuthenticationService
from src.infradata.Maps.AdditionalInfoUserMap import AdditionalInfoUserMap


class UserController(IUserController):
    def __init__(self,
                 user_menagement_service: IUserManagementService,
                 user_authentication_service: IUserAuthenticationService,
                 user_confirmation_service: IUserConfirmationService,
                 user_create_validate: IUserCreateValidate
                 ) -> None:
        self.__user_menagement_service = user_menagement_service
        self.__user_authentication_service = user_authentication_service
        self.__user_confirmation_service = user_confirmation_service
        self.__user_create_validate = user_create_validate

    def create_async(self, http_request: HttpRequest) -> HttpResponse:
        result = self.__user_create_validate.user_create_validate(
            http_request.body)

        if not result.IsSuccess:
            return HttpResponse(
                status_code=422,
                body={"data": result.Data}
            )

        name = http_request.body["name"]
        email = http_request.body["email"]
        cpf = http_request.body["cpf"]
        password = http_request.body["password"]

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

        user_DTO = UserDTO(
            None, name, email, cpf, None, 0, None, birthDateString)

        additional_info_user_DTO = AdditionalInfoUserDTO(
            None,
            None,
            None,
            birthDateString,
            gender,
            phone,
            cep,
            logradouro,
            numero,
            complemento,
            referencia,
            bairro,
            estado,
            cidade
        )

        response = self.__user_menagement_service.create_async(
            user_DTO,  additional_info_user_DTO, password)

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

    def login_user(self, http_request: HttpRequest) -> HttpResponse:
        cpfOrEmail = http_request.path_params["cpfOrEmail"]
        password = http_request.path_params["password"]

        response = self.__user_authentication_service.login(
            cpfOrEmail, password)

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

    def verfic_token(self, http_request: HttpRequest) -> HttpResponse:
        code = http_request.path_params["code"]
        password = http_request.path_params["guidId"]

        response = self.__user_authentication_service.verfic_token(
            code, password)

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

    def get_confirm_token(self, http_request: HttpRequest) -> HttpResponse:
        token = http_request.path_params["token"]

        response = self.__user_confirmation_service.get_confirm_token(token)

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
