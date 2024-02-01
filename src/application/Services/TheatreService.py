from datetime import datetime
import uuid
from src.application.DTOs.RegionDTO import RegionDTO
from src.application.DTOs.TheatreDTO import TheatreDTO
from src.application.Services.Interfaces.IRegionService import IRegionService
from src.application.Services.Interfaces.IRegionTheatreService import IRegionTheatreService
from src.application.Services.Interfaces.ITheatreService import ITheatreService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.ITheatreRepository import ITheatreRepository
from src.infradata.CloudinaryConfig.CloudinaryCreate import CloudinaryCreate
from src.infradata.Maps.TheatreMap import TheatreMap
from src.infradata.UtilityExternal.Interface.ICloudinaryUti import ICloudinaryUti


class TheatreService(ITheatreService):
    def __init__(self, theatre_repository: ITheatreRepository, region_service: IRegionService, region_theatre_service: IRegionTheatreService, cloudinary_uti: ICloudinaryUti) -> None:
        self.__theatre_repository = theatre_repository
        self.__region_service = region_service
        self.__region_theatre_service = region_theatre_service
        self.__cloudinary_uti = cloudinary_uti

    def get_all_theatre_by_state_name(self, state_name: str) -> ResponseWrapper:
        result_region_id = self.__region_service.get_id_by_name_state(
            state_name)

        if not result_region_id.IsSuccess:
            return result_region_id

        data_region: RegionDTO = result_region_id.Data

        theatre_all = self.__theatre_repository.get_all_theatre_by_region_id(
            data_region["id"])

        if not theatre_all.IsSuccess:
            return theatre_all

        return theatre_all

    def create(self, theatre_DTO: TheatreDTO) -> ResponseWrapper:
        if theatre_DTO == None:
            return ResponseWrapper.fail("error dto null")

        new_guid = uuid.uuid4()
        guid_str = str(new_guid)

        result_create_cloudinary = self.__cloudinary_uti.create_img(
            theatre_DTO.Base64Img, 590, 320)

        if not result_create_cloudinary.IsSuccess:
            return result_create_cloudinary

        create_img_base64: CloudinaryCreate = result_create_cloudinary.Data

        theatre_DTO.set_id(guid_str)
        theatre_DTO.add_imgUrl_PublicId(
            create_img_base64.img_url, create_img_base64.public_id)

        parts = theatre_DTO.DataString.split('/')
        year_and_hour_minute = parts[2].split(" ")
        year = int(year_and_hour_minute[0])
        month = int(parts[1])
        day = int(parts[0])

        hour, minute = map(int, year_and_hour_minute[1].split(":"))

        data = datetime(year, month, day, hour, minute)

        theatre_DTO.set_date(data)

        theatre_map = TheatreMap()
        theatre_map.insert_value_attribute(theatre_DTO)

        result_create = self.__theatre_repository.create(theatre_map)

        return result_create

    def delete(self, theatre_id: str) -> ResponseWrapper:
        theatre_get_result = self.__theatre_repository.get_by_id(theatre_id)

        if not theatre_get_result.IsSuccess:
            return theatre_get_result

        if theatre_get_result.Data == None:
            return ResponseWrapper.fail("not exist theatre")

        result_delete_RegionTheatre = self.__region_theatre_service.delete(
            theatre_id)

        if not result_delete_RegionTheatre.IsSuccess:
            return result_delete_RegionTheatre

        delete_theater_result = self.__theatre_repository.delete(theatre_id)

        if not delete_theater_result.IsSuccess:
            return delete_theater_result

        theater_dto_delete: TheatreDTO = delete_theater_result.Data

        result_delete_img = self.__cloudinary_uti.delete_img(
            theater_dto_delete["publicId"])

        if not result_delete_img.IsSuccess:
            return result_delete_img

        return delete_theater_result

    def update_theatre_img(self, theatre_DTO: TheatreDTO) -> ResponseWrapper:
        theatre_update_result = self.__theatre_repository.get_by_id_only_publicId(
            theatre_DTO.Id)

        if not theatre_update_result.IsSuccess:
            return theatre_update_result

        if theatre_update_result.Data == None:
            return ResponseWrapper.fail("theatre not exist")

        theatre_update: TheatreDTO = theatre_update_result.Data

        result_delete_img = self.__cloudinary_uti.delete_img(
            theatre_update.PublicId)

        if not result_delete_img.IsSuccess:
            return result_delete_img

        result_create_img = self.__cloudinary_uti.create_img(
            theatre_DTO.Base64Img, 590, 320)

        if not result_create_img.IsSuccess:
            return result_create_img

        create_img_base64: CloudinaryCreate = result_create_img.Data

        theatre_DTO.add_imgUrl_PublicId(
            create_img_base64.img_url, create_img_base64.public_id)

        result_update_theatre = self.__theatre_repository.update(theatre_DTO)

        if not result_update_theatre.IsSuccess:
            return result_update_theatre

        return result_update_theatre
