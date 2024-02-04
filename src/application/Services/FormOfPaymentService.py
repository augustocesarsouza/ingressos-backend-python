import uuid
from src.application.DTOs.FormOfPaymentDTO import FormOfPaymentDTO
from src.application.Services.Interfaces.IFormOfPaymentService import IFormOfPaymentService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IFormOfPaymentRepository import IFormOfPaymentRepository
from src.infradata.Maps.FormOfPaymentMap import FormOfPaymentMap


class FormOfPaymentService(IFormOfPaymentService):
    def __init__(self, form_of_payment_repository: IFormOfPaymentRepository) -> None:
        self.__form_of_payment_reposiory = form_of_payment_repository

    def get_movie_Id_info(self, movie_id: str) -> ResponseWrapper:
        list_form_of_payment = self.__form_of_payment_reposiory.get_movie_Id_info(
            movie_id)
        return list_form_of_payment

    def create(self, form_of_payment_dto: FormOfPaymentDTO) -> ResponseWrapper:
        if form_of_payment_dto == None:
            return ResponseWrapper.fail("dto informed is null")

        new_guid = uuid.uuid4()
        guid_str = str(new_guid)

        form_of_payment_map = FormOfPaymentMap(
            Id=guid_str, FormName=form_of_payment_dto.FormName, Price=form_of_payment_dto.Price, MovieId=form_of_payment_dto.MovieId)

        result_create_form_of_payment = self.__form_of_payment_reposiory.create(
            form_of_payment_map)

        return result_create_form_of_payment
