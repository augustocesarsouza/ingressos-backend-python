from abc import ABC, abstractmethod

from src.application.Services.ResponseWrapper import ResponseWrapper


class IUserConfirmationService(ABC):

    @abstractmethod
    def get_confirm_token(self, token: str) -> ResponseWrapper:
        pass
