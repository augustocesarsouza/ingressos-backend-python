from src.application.DTOs.TheatreDTO import TheatreDTO
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.ITheatreRepository import ITheatreRepository
from src.infradata.Context.ApplicationDbContext import ApplicationDbContext
from src.infradata.Maps.RegionTheatreMap import RegionTheatreMap
from src.infradata.Maps.TheatreMap import TheatreMap
from sqlalchemy.exc import SQLAlchemyError


class TheatreRepository(ITheatreRepository):

    @classmethod
    def get_by_id(cls, theatre_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                theatre = (
                    database.session
                    .query(TheatreMap.Id, TheatreMap.Title)
                    .filter(TheatreMap.Id == theatre_id)
                    .first()
                )

                theatre_DTO = TheatreDTO(id=theatre.Id, title=theatre.Title, description=None, data=None, location=None, typeOfAttraction=None,
                                         category=None, imgUrl=None, publicId=None, base_64_img=None, dataString=None).to_dict()

                database.session.commit()
                return ResponseWrapper.ok(theatre_DTO)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def get_by_id_only_publicId(cls, theatre_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                user = (
                    database.session
                    .query(TheatreMap.PublicId)
                    .filter(TheatreMap.Id == theatre_id)
                    .first()
                )
                database.session.commit()
                return ResponseWrapper.ok(user)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def get_by_id_all_props(cls, theatre_id: str) -> ResponseWrapper:
        pass

    @classmethod
    def get_all_theatre_by_region_id(cls, region_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                theatres = (
                    database.session
                    .query(TheatreMap)
                    .join(RegionTheatreMap, TheatreMap.Id == RegionTheatreMap.TheatreId)
                    .filter(RegionTheatreMap.RegionId == region_id)
                    .with_entities(
                        TheatreMap.Id, TheatreMap.Title, TheatreMap.Data, TheatreMap.Location, TheatreMap.ImgUrl
                    ).all()
                )
                database.session.commit()

                if theatres != None:
                    array = []

                    for item in theatres:
                        data_string = str(item.Data)
                        data_hour_minute = data_string.split(" ")

                        obj = {
                            "id": item.Id,
                            "title": item.Title,
                            "data": f"{data_hour_minute[0]}T{data_hour_minute[1]}",
                            "location": item.Location,
                            "imgUrl": item.ImgUrl
                        }
                        array.append(obj)

                    return ResponseWrapper.ok(array)
                else:
                    return ResponseWrapper.ok(theatres)

            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def create(cls, theatre: TheatreMap) -> ResponseWrapper:
        with ApplicationDbContext() as database:

            theatre_DTO = TheatreDTO(id=None, title=theatre.Title, description=None, data=None, location=theatre.Location, typeOfAttraction=None,
                                     category=None, imgUrl=None, publicId=None, base_64_img=None, dataString=None).to_dict()

            try:
                database.session.begin()
                database.session.add(theatre)
                database.session.commit()
                return ResponseWrapper.ok(theatre_DTO)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def delete(cls, id_theatre: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()

                theatre = database.session.query(
                    TheatreMap).filter_by(Id=id_theatre).first()

                database.session.delete(theatre)
                database.session.commit()

                theatre_DTO = TheatreDTO(id=theatre.Id, title=theatre.Title, description=None, data=None, location=theatre.Location, typeOfAttraction=None,
                                         category=None, imgUrl=None, publicId=theatre.PublicId, base_64_img=None, dataString=None).to_dict()

                return ResponseWrapper.ok(theatre_DTO)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def update(cls, theatre_DTO: TheatreDTO) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                theatre = database.session.query(TheatreMap).filter(
                    TheatreMap.Id == theatre_DTO.Id).first()

                if theatre != None:
                    theatre.ImgUrl = theatre_DTO.ImgUrl
                    theatre.PublicId = theatre_DTO.PublicId
                database.session.commit()
                return ResponseWrapper.ok(theatre_DTO.to_dict())
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")
