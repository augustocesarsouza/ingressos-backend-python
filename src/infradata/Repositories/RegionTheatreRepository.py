from src.application.DTOs.RegionTheatreDTO import RegionTheatreDTO
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IRegionTheatreRepository import IRegionTheatreRepository
from src.infradata.Context.ApplicationDbContext import ApplicationDbContext
from src.infradata.Maps.RegionTheatreMap import RegionTheatreMap
from sqlalchemy.exc import SQLAlchemyError


class RegionTheatreRepository(IRegionTheatreRepository):

    @classmethod
    def get_by_theatre_id(cls, theatre_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                theatres = (
                    database.session
                    .query(RegionTheatreMap)
                    .filter(RegionTheatreMap.TheatreId == theatre_id)
                    .all()
                )

                theatres_dtos = []

                for el in theatres:
                    theatre_DTO = RegionTheatreDTO(
                        id=el.Id, theatreId=el.TheatreId, regionId=el.RegionId).to_dict()
                    theatres_dtos.append(theatre_DTO)

                database.session.commit()
                return ResponseWrapper.ok(theatres_dtos)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def delete(cls, region_theatre_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()

                theatre = database.session.query(
                    RegionTheatreMap).filter_by(Id=region_theatre_id).first()

                database.session.delete(theatre)
                database.session.commit()

                theatre_DTO = RegionTheatreDTO(
                    id=theatre.Id, theatreId=theatre.TheatreId, regionId=theatre.RegionId).to_dict()

                return ResponseWrapper.ok(theatre_DTO)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")
