from abc import ABC, abstractmethod
from src.application.DTOs.AdditionalInfoUserDTO import AdditionalInfoUserDTO
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.infradata.Maps.AdditionalInfoUserMap import AdditionalInfoUserMap


class IAdditionalInfoUserRepository(ABC):

    @abstractmethod
    def create_info(cls, infoUser: AdditionalInfoUserMap) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_info_user(cls, id_guid: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def get_by_id_guid_user(cls, id_guid: str) -> ResponseWrapper:
        pass

    @abstractmethod
    def update_async(cls, infoUser: AdditionalInfoUserDTO) -> ResponseWrapper:
        pass
