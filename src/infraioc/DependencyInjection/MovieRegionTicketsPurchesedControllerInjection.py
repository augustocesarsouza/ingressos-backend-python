from src.api.Controllers.MovieRegionTicketsPurchesedController import MovieRegionTicketsPurchesedController
from src.api.ControllersInterface.IMovieRegionTicketsPurchesedController import IMovieRegionTicketsPurchesedController
from src.application.Services.MovieRegionTicketsPurchesedService import MovieRegionTicketsPurchesedService
from src.api.Validators.MovieRegionTicketsPurchesedValidate import MovieRegionTicketsPurchesedValidate
from src.infradata.Repositories.MovieRegionTicketsPurchesedRepository import MovieRegionTicketsPurchesedRepository


def movie_region_controller_injection() -> IMovieRegionTicketsPurchesedController:
    movie_region_tickets_purchesed_repository = MovieRegionTicketsPurchesedRepository()

    movie_region_tickets_purchesed_service = MovieRegionTicketsPurchesedService(
        movie_region_tickets_purchesed_repository)
    movie_region_tickets_purchesed_validate = MovieRegionTicketsPurchesedValidate()

    controller = MovieRegionTicketsPurchesedController(
        movie_region_tickets_purchesed_service, movie_region_tickets_purchesed_validate)
    return controller
