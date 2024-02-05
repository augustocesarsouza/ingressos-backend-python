from abc import ABC, abstractmethod
from src.application.DTOs.AdditionalInfoUserDTO import AdditionalInfoUserDTO
from src.application.Services.ResponseWrapper import ResponseWrapper


class IAdditionalInfoUserService(ABC):

    @abstractmethod
    def get_info_user(cls, id_guid: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def create_info(cls, infoUser: AdditionalInfoUserDTO) -> ResponseWrapper:
        pass

    @abstractmethod
    def update_async(cls, infoUser: AdditionalInfoUserDTO, password: str) -> ResponseWrapper:
        pass
