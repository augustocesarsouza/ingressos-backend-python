from src.application.Services.Interfaces.IRegionTheatreService import IRegionTheatreService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IRegionTheatreRepository import IRegionTheatreRepository


class RegionTheatreService(IRegionTheatreService):
    def __init__(self, region_theatre_repository: IRegionTheatreRepository) -> None:
        self.__region_theatre_repository = region_theatre_repository

    def delete(self, theatre_id: str) -> ResponseWrapper:
        theatre_all_movieTheatre = self.__region_theatre_repository.get_by_theatre_id(
            theatre_id)

        if not theatre_all_movieTheatre.IsSuccess:
            return theatre_all_movieTheatre

        if len(theatre_all_movieTheatre.Data) <= 0:
            return ResponseWrapper.ok("não existe essa junção no movietheatre")

        theatre_all = theatre_all_movieTheatre.Data

        for el in theatre_all:
            self.__region_theatre_repository.delete(el["id"])

        return ResponseWrapper.ok("tudo deletado")
