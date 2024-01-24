from abc import ABC, abstractmethod

from src.application.Services.ResponseWrapper import ResponseWrapper


class ISendEmailUser(ABC):

    def send_email(self, user: dict[str, any]) -> ResponseWrapper:
        pass

    def send_code_random(self, user: dict[str, any], code: int):
        pass
