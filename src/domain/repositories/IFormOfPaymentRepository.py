from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.infradata.Maps.FormOfPaymentMap import FormOfPaymentMap


class IFormOfPaymentRepository(ABC):

    @abstractmethod
    def get_all_form_of_payment_id_by_movie_id(cls, movie_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_movie_Id_info(cls, movie_id: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def create(cls, form_of_payment_map: FormOfPaymentMap) -> ResponseWrapper:
        pass

    @abstractmethod
    def delete(cls, form_of_payment_id: str) -> ResponseWrapper:
        pass
