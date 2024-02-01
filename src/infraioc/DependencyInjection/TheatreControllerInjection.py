
from src.api.Controllers.TheatreController import TheatreController
from src.api.ControllersInterface.ITheatreController import ITheatreController
from src.api.Validators.TheatreValidate import TheatreValidate
from src.application.Services.RegionService import RegionService
from src.application.Services.RegionTheatreService import RegionTheatreService
from src.application.Services.TheatreService import TheatreService
from src.infradata.Repositories.RegionRepository import RegionRepository
from src.infradata.Repositories.RegionTheatreRepository import RegionTheatreRepository
from src.infradata.Repositories.TheatreRepository import TheatreRepository
from src.infradata.UtilityExternal.CloudinaryUti import CloudinaryUti


def theatre_controller_injection() -> ITheatreController:
    theatre_repository = TheatreRepository()
    cloudinary_uti = CloudinaryUti()
    region_theatre_repository = RegionTheatreRepository()

    region_repository = RegionRepository()
    region_theatre_service = RegionTheatreService(region_theatre_repository)
    region_service = RegionService(region_repository)

    theatre_service = TheatreService(
        theatre_repository, region_service, region_theatre_service, cloudinary_uti)
    theatre_validate = TheatreValidate()

    controller = TheatreController(theatre_service, theatre_validate)
    return controller
