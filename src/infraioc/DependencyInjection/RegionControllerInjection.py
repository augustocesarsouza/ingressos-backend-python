from src.api.Controllers.RegionController import RegionController
from src.api.ControllersInterface.IRegionController import IRegionController
from src.application.Services.RegionService import RegionService
from src.infradata.Repositories.RegionRepository import RegionRepository


def region_controller_injection() -> IRegionController:
    region_repository = RegionRepository()
    region_service = RegionService(region_repository)

    controller = RegionController(region_service)
    return controller
