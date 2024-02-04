from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class IFormOfPaymentValidate(ABC):

    @abstractmethod
    def form_of_payment_create_validate(cls, body: any) -> ResponseWrapper:
        pass
