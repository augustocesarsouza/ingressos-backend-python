from src.application.DTOs.RegionDTO import RegionDTO
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IRegionRepository import IRegionRepository
from src.infradata.Context.ApplicationDbContext import ApplicationDbContext
from sqlalchemy.exc import SQLAlchemyError

from src.infradata.Maps.RegionMap import RegionMap


class RegionRepository(IRegionRepository):

    @classmethod
    def get_region_by_id_check_exist(self, region_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                region = (
                    database.session
                    .query(RegionMap.Id)
                    .filter(RegionMap.Id == region_id)
                    .first()
                )

                database.session.commit()
                if region != None:
                    region_DTO = RegionDTO(
                        id=region.Id, state=None, city=None).to_dict()
                    return ResponseWrapper.ok(region_DTO)
                else:
                    return ResponseWrapper.ok(region)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def get_region_id_by_city_name(cls, city: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                region = (
                    database.session
                    .query(RegionMap.Id)
                    .filter(RegionMap.City == city)
                    .first()
                )
                database.session.commit()

                if region != None:
                    region_DTO = RegionDTO(
                        region.Id, None, None).to_dict()
                    return ResponseWrapper.ok(region_DTO)
                else:
                    return ResponseWrapper.ok(region)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def get_id_by_name_state(cls, state: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                region = (
                    database.session
                    .query(RegionMap.Id)
                    .filter(RegionMap.State == state)
                    .first()
                )
                database.session.commit()

                if region != None:
                    region_DTO = RegionDTO(region.Id, None, None).to_dict()
                    return ResponseWrapper.ok(region_DTO)
                else:
                    return ResponseWrapper.ok(region)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")
