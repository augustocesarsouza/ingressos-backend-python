import unittest
from unittest.mock import Mock
from src.application.DTOs.RegionDTO import RegionDTO
from src.application.DTOs.TheatreDTO import TheatreDTO
from src.application.Services.Interfaces.IRegionTheatreService import IRegionTheatreService
from src.application.Services.ResponseWrapper import ResponseWrapper

from src.application.Services.TheatreService import TheatreService
from src.application.Services.Interfaces.IRegionService import IRegionService
from src.domain.repositories.ITheatreRepository import ITheatreRepository
from src.infradata.CloudinaryConfig.CloudinaryCreate import CloudinaryCreate
from src.infradata.UtilityExternal.Interface.ICloudinaryUti import ICloudinaryUti


class Test_TheatreService(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_theatre_repository = Mock(spec=ITheatreRepository)
        self.mock_region_service = Mock(spec=IRegionService)
        self.mock_region_theatre_service = Mock(spec=IRegionTheatreService)
        self.mock_cloudinary_uti = Mock(spec=ICloudinaryUti)

    # test func 'get_all_theatre_by_state_name'
    def test_get_all_theatre_by_state_name_without_error(self):
        region_dto = RegionDTO(
            id="08f0952f-4106-4767-bca9-4b481b2762c0", state=None, city=None).to_dict()

        self.mock_region_service.get_id_by_name_state.return_value = ResponseWrapper.ok(
            region_dto)

        self.mock_theatre_repository.get_all_theatre_by_region_id.return_value = ResponseWrapper.ok(
            "Ok")

        movie_service = TheatreService(self.mock_theatre_repository, self.mock_region_service,
                                       self.mock_region_theatre_service, self.mock_cloudinary_uti)

        result = movie_service.get_all_theatre_by_state_name("São paulo")
        self.assertEqual(result.IsSuccess, True)

    def test_get_all_theatre_by_state_name_with_error_or_not_found_or_database_error(self):
        self.mock_region_service.get_id_by_name_state.return_value = ResponseWrapper.fail(
            "error not fould or database error")

        movie_service = TheatreService(self.mock_theatre_repository, self.mock_region_service,
                                       self.mock_region_theatre_service, self.mock_cloudinary_uti)

        result = movie_service.get_all_theatre_by_state_name("São paulo")
        self.assertEqual(result.IsSuccess, False)

    def test_get_all_theatre_by_state_name_with_error_get_all_theatre(self):
        region_dto = RegionDTO(
            id="08f0952f-4106-4767-bca9-4b481b2762c0", state=None, city=None).to_dict()

        self.mock_region_service.get_id_by_name_state.return_value = ResponseWrapper.ok(
            region_dto)

        self.mock_theatre_repository.get_all_theatre_by_region_id.return_value = ResponseWrapper.fail(
            "error get all theatre")

        movie_service = TheatreService(self.mock_theatre_repository, self.mock_region_service,
                                       self.mock_region_theatre_service, self.mock_cloudinary_uti)

        result = movie_service.get_all_theatre_by_state_name("São paulo")
        self.assertEqual(result.IsSuccess, False)

    # test func 'create'
    def test_create_without_error(self):
        self.mock_cloudinary_uti.create_img.return_value = ResponseWrapper.ok(
            CloudinaryCreate("public_id1", "image_url1"))

        self.mock_theatre_repository.create.return_value = ResponseWrapper.ok(
            "ok")

        theatre_dto = TheatreDTO(id=None, title=None, description=None, data=None, location=None,
                                 typeOfAttraction=None, category=None, imgUrl=None, publicId=None,
                                 base_64_img="base_64_img1", dataString="10/10/1996 16:30")

        theatre_service = TheatreService(self.mock_theatre_repository, self.mock_region_service,
                                         self.mock_region_theatre_service, self.mock_cloudinary_uti)

        result = theatre_service.create(theatre_dto)
        self.assertEqual(result.IsSuccess, True)

    def test_create_with_error_dto_null(self):
        theatre_service = TheatreService(self.mock_theatre_repository, self.mock_region_service,
                                         self.mock_region_theatre_service, self.mock_cloudinary_uti)

        result = theatre_service.create(None)
        self.assertEqual(result.IsSuccess, False)

    def test_create_with_error_create_img_cloudinary(self):
        self.mock_cloudinary_uti.create_img.return_value = ResponseWrapper.fail(
            "error when deleting img")

        theatre_dto = TheatreDTO(id=None, title=None, description=None, data=None, location=None,
                                 typeOfAttraction=None, category=None, imgUrl=None, publicId=None,
                                 base_64_img="base_64_img1", dataString="10/10/1996 16:30")

        theatre_service = TheatreService(self.mock_theatre_repository, self.mock_region_service,
                                         self.mock_region_theatre_service, self.mock_cloudinary_uti)

        result = theatre_service.create(theatre_dto)
        self.assertEqual(result.IsSuccess, False)

    # test func 'delete'
    def test_delete_without_error(self):
        self.mock_theatre_repository.get_by_id.return_value = ResponseWrapper.ok(
            "ok")

        self.mock_region_theatre_service.delete.return_value = ResponseWrapper.ok(
            "delete join theatre and ragion")

        theatre_dto = TheatreDTO(id=None, title=None, description=None, data=None, location=None,
                                 typeOfAttraction=None, category=None, imgUrl=None, publicId="publicId1",
                                 base_64_img=None, dataString=None).to_dict()

        self.mock_theatre_repository.delete.return_value = ResponseWrapper.ok(
            theatre_dto)

        self.mock_cloudinary_uti.delete_img.return_value = ResponseWrapper.ok(
            "image delete cloudinary")

        theatre_service = TheatreService(self.mock_theatre_repository, self.mock_region_service,
                                         self.mock_region_theatre_service, self.mock_cloudinary_uti)

        result = theatre_service.delete("08f0952f-4106-4767-bca9-4b481b2762c0")
        self.assertEqual(result.IsSuccess, True)

    def test_delete_with_error_database(self):
        self.mock_theatre_repository.get_by_id.return_value = ResponseWrapper.fail(
            "error database")

        theatre_service = TheatreService(self.mock_theatre_repository, self.mock_region_service,
                                         self.mock_region_theatre_service, self.mock_cloudinary_uti)

        result = theatre_service.delete("08f0952f-4106-4767-bca9-4b481b2762c0")
        self.assertEqual(result.IsSuccess, False)

    def test_delete_with_error_not_exist(self):
        self.mock_theatre_repository.get_by_id.return_value = ResponseWrapper.ok(
            None)

        theatre_service = TheatreService(self.mock_theatre_repository, self.mock_region_service,
                                         self.mock_region_theatre_service, self.mock_cloudinary_uti)

        result = theatre_service.delete("08f0952f-4106-4767-bca9-4b481b2762c0")
        self.assertEqual(result.IsSuccess, False)
        self.assertEqual(result.Data["message"], "not exist theatre")

    def test_delete_with_error_cannot_not_delete_join_between_region_and_theatre(self):
        self.mock_theatre_repository.get_by_id.return_value = ResponseWrapper.ok(
            "ok")

        self.mock_region_theatre_service.delete.return_value = ResponseWrapper.fail(
            "delete join theatre and ragion")

        theatre_service = TheatreService(self.mock_theatre_repository, self.mock_region_service,
                                         self.mock_region_theatre_service, self.mock_cloudinary_uti)

        result = theatre_service.delete("08f0952f-4106-4767-bca9-4b481b2762c0")
        self.assertEqual(result.IsSuccess, False)

    def test_delete_with_error_when_delete_theatre(self):
        self.mock_theatre_repository.get_by_id.return_value = ResponseWrapper.ok(
            "ok")

        self.mock_region_theatre_service.delete.return_value = ResponseWrapper.ok(
            "delete join theatre and ragion")

        self.mock_theatre_repository.delete.return_value = ResponseWrapper.fail(
            "error when delete theatre")

        theatre_service = TheatreService(self.mock_theatre_repository, self.mock_region_service,
                                         self.mock_region_theatre_service, self.mock_cloudinary_uti)

        result = theatre_service.delete("08f0952f-4106-4767-bca9-4b481b2762c0")
        self.assertEqual(result.IsSuccess, False)

    def test_delete_with_error_cloudinary_delete_img(self):
        self.mock_theatre_repository.get_by_id.return_value = ResponseWrapper.ok(
            "ok")

        self.mock_region_theatre_service.delete.return_value = ResponseWrapper.ok(
            "delete join theatre and ragion")

        theatre_dto = TheatreDTO(id=None, title=None, description=None, data=None, location=None,
                                 typeOfAttraction=None, category=None, imgUrl=None, publicId="publicId1",
                                 base_64_img=None, dataString=None).to_dict()

        self.mock_theatre_repository.delete.return_value = ResponseWrapper.ok(
            theatre_dto)

        self.mock_cloudinary_uti.delete_img.return_value = ResponseWrapper.fail(
            "error when delete img cloudinary")

        theatre_service = TheatreService(self.mock_theatre_repository, self.mock_region_service,
                                         self.mock_region_theatre_service, self.mock_cloudinary_uti)

        result = theatre_service.delete("08f0952f-4106-4767-bca9-4b481b2762c0")
        self.assertEqual(result.IsSuccess, False)

    # test func 'update_theatre_img'
    def test_delete_without_error(self):
        theatre_update = TheatreDTO(id=None, title=None, description=None, data=None, location=None,
                                    typeOfAttraction=None, category=None, imgUrl=None, publicId=None,
                                    base_64_img=None, dataString=None)

        self.mock_theatre_repository.get_by_id_only_publicId.return_value = ResponseWrapper.ok(
            theatre_update)

        self.mock_cloudinary_uti.delete_img.return_value = ResponseWrapper.ok(
            "delete Successfully")

        self.mock_cloudinary_uti.create_img.return_value = ResponseWrapper.ok(
            CloudinaryCreate("public_id1", "image_url1"))

        self.mock_theatre_repository.update.return_value = ResponseWrapper.ok(
            "updated Successfully")

        theatre_dto = TheatreDTO(id="08f0952f-4106-4767-bca9-4b481b2762c0", title=None, description=None, data=None, location=None,
                                 typeOfAttraction=None, category=None, imgUrl=None, publicId="publicId1",
                                 base_64_img="base_64_img1", dataString=None)

        theatre_service = TheatreService(self.mock_theatre_repository, self.mock_region_service,
                                         self.mock_region_theatre_service, self.mock_cloudinary_uti)

        result = theatre_service.update_theatre_img(theatre_dto)
        self.assertEqual(result.IsSuccess, True)

    def test_delete_with_error_database(self):
        self.mock_theatre_repository.get_by_id_only_publicId.return_value = ResponseWrapper.fail(
            "error database")

        theatre_dto = TheatreDTO(id="08f0952f-4106-4767-bca9-4b481b2762c0", title=None, description=None, data=None, location=None,
                                 typeOfAttraction=None, category=None, imgUrl=None, publicId="publicId1",
                                 base_64_img="base_64_img1", dataString=None)

        theatre_service = TheatreService(self.mock_theatre_repository, self.mock_region_service,
                                         self.mock_region_theatre_service, self.mock_cloudinary_uti)

        result = theatre_service.update_theatre_img(theatre_dto)
        self.assertEqual(result.IsSuccess, False)

    def test_delete_with_error_theatre_not_exist(self):
        self.mock_theatre_repository.get_by_id_only_publicId.return_value = ResponseWrapper.ok(
            None)

        theatre_dto = TheatreDTO(id="08f0952f-4106-4767-bca9-4b481b2762c0", title=None, description=None, data=None, location=None,
                                 typeOfAttraction=None, category=None, imgUrl=None, publicId="publicId1",
                                 base_64_img="base_64_img1", dataString=None)

        theatre_service = TheatreService(self.mock_theatre_repository, self.mock_region_service,
                                         self.mock_region_theatre_service, self.mock_cloudinary_uti)

        result = theatre_service.update_theatre_img(theatre_dto)
        self.assertEqual(result.IsSuccess, False)

    def test_delete_with_error_delete_img_cloudinary(self):
        theatre_update = TheatreDTO(id=None, title=None, description=None, data=None, location=None,
                                    typeOfAttraction=None, category=None, imgUrl=None, publicId=None,
                                    base_64_img=None, dataString=None)

        self.mock_theatre_repository.get_by_id_only_publicId.return_value = ResponseWrapper.ok(
            theatre_update)

        self.mock_cloudinary_uti.delete_img.return_value = ResponseWrapper.fail(
            "error when delete img cloudinary")

        theatre_dto = TheatreDTO(id="08f0952f-4106-4767-bca9-4b481b2762c0", title=None, description=None, data=None, location=None,
                                 typeOfAttraction=None, category=None, imgUrl=None, publicId="publicId1",
                                 base_64_img="base_64_img1", dataString=None)

        theatre_service = TheatreService(self.mock_theatre_repository, self.mock_region_service,
                                         self.mock_region_theatre_service, self.mock_cloudinary_uti)

        result = theatre_service.update_theatre_img(theatre_dto)
        self.assertEqual(result.IsSuccess, False)

    def test_delete_with_error_create_img_cloudinary(self):
        theatre_update = TheatreDTO(id=None, title=None, description=None, data=None, location=None,
                                    typeOfAttraction=None, category=None, imgUrl=None, publicId=None,
                                    base_64_img=None, dataString=None)

        self.mock_theatre_repository.get_by_id_only_publicId.return_value = ResponseWrapper.ok(
            theatre_update)

        self.mock_cloudinary_uti.delete_img.return_value = ResponseWrapper.ok(
            "delete Successfully")

        self.mock_cloudinary_uti.create_img.return_value = ResponseWrapper.fail(
            "error when create img cloudinary")

        theatre_dto = TheatreDTO(id="08f0952f-4106-4767-bca9-4b481b2762c0", title=None, description=None, data=None, location=None,
                                 typeOfAttraction=None, category=None, imgUrl=None, publicId="publicId1",
                                 base_64_img="base_64_img1", dataString=None)

        theatre_service = TheatreService(self.mock_theatre_repository, self.mock_region_service,
                                         self.mock_region_theatre_service, self.mock_cloudinary_uti)

        result = theatre_service.update_theatre_img(theatre_dto)
        self.assertEqual(result.IsSuccess, False)

    def test_delete_with_error_updated_theatre(self):
        theatre_update = TheatreDTO(id=None, title=None, description=None, data=None, location=None,
                                    typeOfAttraction=None, category=None, imgUrl=None, publicId=None,
                                    base_64_img=None, dataString=None)

        self.mock_theatre_repository.get_by_id_only_publicId.return_value = ResponseWrapper.ok(
            theatre_update)

        self.mock_cloudinary_uti.delete_img.return_value = ResponseWrapper.ok(
            "delete Successfully")

        self.mock_cloudinary_uti.create_img.return_value = ResponseWrapper.ok(
            CloudinaryCreate("public_id1", "image_url1"))

        self.mock_theatre_repository.update.return_value = ResponseWrapper.fail(
            "error update theatre")

        theatre_dto = TheatreDTO(id="08f0952f-4106-4767-bca9-4b481b2762c0", title=None, description=None, data=None, location=None,
                                 typeOfAttraction=None, category=None, imgUrl=None, publicId="publicId1",
                                 base_64_img="base_64_img1", dataString=None)

        theatre_service = TheatreService(self.mock_theatre_repository, self.mock_region_service,
                                         self.mock_region_theatre_service, self.mock_cloudinary_uti)

        result = theatre_service.update_theatre_img(theatre_dto)
        self.assertEqual(result.IsSuccess, False)
