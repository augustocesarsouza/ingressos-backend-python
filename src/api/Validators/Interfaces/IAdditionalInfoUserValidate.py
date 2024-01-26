from abc import ABC, abstractmethod

from src.application.Services.ResponseWrapper import ResponseWrapper


class IAdditionalInfoUserValidate(ABC):

    @abstractmethod
    def user_update_validate(self, body: any) -> ResponseWrapper:
        pass
