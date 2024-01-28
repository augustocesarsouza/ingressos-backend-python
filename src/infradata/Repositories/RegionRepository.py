from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IRegionRepository import IRegionRepository
from src.infradata.Context.ApplicationDbContext import ApplicationDbContext
from sqlalchemy.exc import SQLAlchemyError

from src.infradata.Maps.RegionMap import RegionMap


class RegionRepository(IRegionRepository):

    def get_region_id(cls, region: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                user = (
                    database.session
                    .query(RegionMap.Id)
                    .filter(RegionMap.City == region)
                    .first()
                )
                database.session.commit()
                return ResponseWrapper.ok(user)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    def get_id_by_name_city(cls, state: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                user = (
                    database.session
                    .query(RegionMap.Id)
                    .filter(RegionMap.State == state)
                    .first()
                )
                database.session.commit()
                return ResponseWrapper.ok(user)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")
