from abc import ABC, abstractmethod
from src.application.DTOs.FormOfPaymentDTO import FormOfPaymentDTO
from src.application.Services.ResponseWrapper import ResponseWrapper


class IFormOfPaymentService(ABC):

    @abstractmethod
    def get_movie_Id_info(cls, movie_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def create(cls, form_of_payment_dto: FormOfPaymentDTO) -> ResponseWrapper:
        pass

    @abstractmethod
    def delete(cls, movie_id: str) -> ResponseWrapper:
        pass
