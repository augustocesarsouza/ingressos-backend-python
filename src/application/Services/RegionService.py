from src.application.Services.Interfaces.IRegionService import IRegionService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IRegionRepository import IRegionRepository


class RegionService(IRegionService):
    def __init__(self, region_repository: IRegionRepository) -> None:
        self.__region_repository = region_repository

    def get_city_id(self, city: str) -> ResponseWrapper:
        region_obj = self.__region_repository.get_city_id(city)

        if region_obj.Data == None:
            return ResponseWrapper.fail("not found region")

        if not region_obj.IsSuccess:
            # erro no banco
            return region_obj

        return region_obj

    def get_id_by_name_state(self, state: str) -> ResponseWrapper:
        region_obj = self.__region_repository.get_id_by_name_state(state)

        if region_obj.Data == None:
            return ResponseWrapper.fail("not found region")

        if not region_obj.IsSuccess:
            # erro no banco
            return region_obj

        return region_obj
