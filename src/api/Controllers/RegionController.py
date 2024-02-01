from src.api.ControllersInterface.IRegionController import IRegionController
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.HttpTypes.HttpResponse import HttpResponse
from src.application.Services.Interfaces.IRegionService import IRegionService


class RegionController(IRegionController):
    def __init__(self, region_service: IRegionService) -> None:
        self.__region_service = region_service

    def get_all_movie_by_region_id(self, http_request: HttpRequest) -> HttpResponse:
        state = http_request.path_params["state"]

        get_id_by_name_result = self.__region_service.get_id_by_name_state(
            state)

        if get_id_by_name_result.IsSuccess:
            return HttpResponse(
                status_code=200,
                body={"data": get_id_by_name_result.Data}
            )
        else:
            return HttpResponse(
                status_code=400,
                body={"data": get_id_by_name_result.Data}
            )
