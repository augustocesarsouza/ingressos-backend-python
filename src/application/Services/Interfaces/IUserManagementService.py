from abc import ABC, abstractmethod
from src.application.DTOs.UserDTO import UserDTO
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.infradata.Maps.AdditionalInfoUserMap import AdditionalInfoUserMap


class IUserManagementService(ABC):

    @abstractmethod
    def create_async(self, user_DTO: UserDTO, additional_info_user_map: AdditionalInfoUserMap, password: str) -> ResponseWrapper:
        pass
