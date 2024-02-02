from src.api.Controllers.CinemaController import CinemaController
from src.api.ControllersInterface.ICinemaController import ICinemaController
from src.application.Services.CinemaService import CinemaService
from src.api.Validators.CinemaValidate import CinemaValidate
from src.infradata.Repositories.CinemaRepository import CinemaRepository


def cinema_controller_injection() -> ICinemaController:
    cinema_repository = CinemaRepository()

    cinema_service = CinemaService(cinema_repository)
    cinema_validate = CinemaValidate()

    controller = CinemaController(cinema_service, cinema_validate)
    return controller
