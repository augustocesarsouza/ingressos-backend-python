import unittest
from unittest.mock import Mock

from src.application.Services.RegionService import RegionService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IRegionRepository import IRegionRepository


class Test_RegionService(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_region_repository = Mock(spec=IRegionRepository)

    # test func 'get_region_id_by_city_name'
    def test_get_region_id_by_city_name_without_error(self):
        self.mock_region_repository.get_region_id_by_city_name.return_value = ResponseWrapper.ok(
            "ok")

        region_service = RegionService(self.mock_region_repository)

        result = region_service.get_region_id_by_city_name("Campinas")
        self.assertEqual(result.IsSuccess, True)

    def test_get_region_id_by_city_name_error_not_exit_database(self):
        self.mock_region_repository.get_region_id_by_city_name.return_value = ResponseWrapper.ok(
            None)

        region_service = RegionService(self.mock_region_repository)

        result = region_service.get_region_id_by_city_name("Campinas")
        self.assertEqual(result.IsSuccess, False)
        self.assertEqual(result.Data["message"], "not found region")

    def test_get_region_id_by_city_name_error_database(self):
        self.mock_region_repository.get_region_id_by_city_name.return_value = ResponseWrapper.fail(
            "database error")

        region_service = RegionService(self.mock_region_repository)

        result = region_service.get_region_id_by_city_name("Campinas")
        self.assertEqual(result.IsSuccess, False)

    # test func 'get_id_by_name_state'
    def test_get_id_by_name_state_without_error(self):
        self.mock_region_repository.get_id_by_name_state.return_value = ResponseWrapper.ok(
            "ok")

        region_service = RegionService(self.mock_region_repository)

        result = region_service.get_id_by_name_state("São Paulo")
        self.assertEqual(result.IsSuccess, True)

    def test_get_id_by_name_state_not_exit_database(self):
        self.mock_region_repository.get_id_by_name_state.return_value = ResponseWrapper.ok(
            None)

        region_service = RegionService(self.mock_region_repository)

        result = region_service.get_id_by_name_state("São Paulo")
        self.assertEqual(result.IsSuccess, False)
        self.assertEqual(result.Data["message"], "not found region")

    def test_get_id_by_name_state_database(self):
        self.mock_region_repository.get_id_by_name_state.return_value = ResponseWrapper.fail(
            "database error")

        region_service = RegionService(self.mock_region_repository)

        result = region_service.get_id_by_name_state("São Paulo")
        self.assertEqual(result.IsSuccess, False)
