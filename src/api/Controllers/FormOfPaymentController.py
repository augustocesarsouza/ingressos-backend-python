from src.api.ControllersInterface.IFormOfPaymentController import IFormOfPaymentController
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.HttpTypes.HttpResponse import HttpResponse
from src.api.Validators.Interfaces.IFormOfPaymentValidate import IFormOfPaymentValidate
from src.application.DTOs.FormOfPaymentDTO import FormOfPaymentDTO
from src.application.Services.Interfaces.IFormOfPaymentService import IFormOfPaymentService


class FormOfPaymentController(IFormOfPaymentController):
    def __init__(self, form_of_payment_service: IFormOfPaymentService, form_of_payment_validate: IFormOfPaymentValidate) -> None:
        self.__form_of_payment_service = form_of_payment_service
        self.__form_of_payment_validate = form_of_payment_validate

    def get_movie_Id_info(self, http_request: HttpRequest) -> HttpResponse:
        movie_id = http_request.path_params["movieid"]

        result_get_list_form_of_payment = self.__form_of_payment_service.get_movie_Id_info(
            movie_id)

        if result_get_list_form_of_payment.IsSuccess:
            return HttpResponse(
                status_code=200,
                body={"data": result_get_list_form_of_payment.Data}
            )
        else:
            return HttpResponse(
                status_code=400,
                body={"data": result_get_list_form_of_payment.Data}
            )

    def create(self, http_request: HttpRequest) -> HttpResponse:
        result_validate_body = self.__form_of_payment_validate.form_of_payment_create_validate(
            http_request.body)

        if not result_validate_body.IsSuccess:
            return HttpResponse(
                status_code=422,
                body={"data": result_validate_body.Data}
            )

        form_name = http_request.body["formName"]
        price = http_request.body["price"]
        movie_id = http_request.body["movieId"]

        form_of_payment_dto = FormOfPaymentDTO(
            id=None, formName=form_name, price=price, movieId=movie_id)

        result_create = self.__form_of_payment_service.create(
            form_of_payment_dto)

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
