import unittest
from unittest.mock import Mock

from src.application.DTOs.RegionTheatreDTO import RegionTheatreDTO
from src.application.Services.RegionTheatreService import RegionTheatreService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IRegionTheatreRepository import IRegionTheatreRepository


class RegionTheatreServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_region_theatre_repository = Mock(
            spec=IRegionTheatreRepository)

    # test func 'delete'
    def test_delete_without_error(self):
        theatre_region_all = []

        theatre_DTO = RegionTheatreDTO(
            id="40b39ddc-99af-4adf-a742-b89661e63779", theatreId="09eca8d8-6aa5-465e-a5ca-5af22221de20", regionId="fe22380e-584c-41f6-9086-efb9a2a27857").to_dict()

        theatre_region_all.append(theatre_DTO)

        self.mock_region_theatre_repository.get_by_theatre_id.return_value = ResponseWrapper.ok(
            theatre_region_all)

        region_theatre_service = RegionTheatreService(
            self.mock_region_theatre_repository)

        result = region_theatre_service.delete(
            "bb610fbe-539b-40d5-95f5-0ab5700b9475")

        self.assertEqual(result.IsSuccess, True)
        self.assertEqual(result.Data, "tudo deletado")

    def test_delete_with_error_database(self):
        self.mock_region_theatre_repository.get_by_theatre_id.return_value = ResponseWrapper.fail(
            "error database")

        region_theatre_service = RegionTheatreService(
            self.mock_region_theatre_repository)

        result = region_theatre_service.delete(
            "bb610fbe-539b-40d5-95f5-0ab5700b9475")

        self.assertEqual(result.IsSuccess, False)

    def test_delete_with_error_not_exist_registers(self):
        theatre_region_all = []

        self.mock_region_theatre_repository.get_by_theatre_id.return_value = ResponseWrapper.ok(
            theatre_region_all)

        region_theatre_service = RegionTheatreService(
            self.mock_region_theatre_repository)

        result = region_theatre_service.delete(
            "bb610fbe-539b-40d5-95f5-0ab5700b9475")

        self.assertEqual(result.IsSuccess, True)
        self.assertEqual(result.Data, "não existe essa junção no movietheatre")
