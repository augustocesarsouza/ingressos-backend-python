from abc import ABC, abstractmethod
from src.application.Services.ResponseWrapper import ResponseWrapper


class ISendEmailBrevo(ABC):

    @abstractmethod
    def send_email(cls, user: dict[str, any], url: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def send_code(cls, user: dict[str, any], code_randon: int) -> ResponseWrapper:
        pass
