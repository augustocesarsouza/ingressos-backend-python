from src.api.Controllers.MovieController import MovieController
from src.api.ControllersInterface.IMovieController import IMovieController
from src.api.Validators.MovieValidate import MovieValidate
from src.infradata.UtilityExternal.CloudinaryUti import CloudinaryUti
from src.application.Services.MovieRegionTicketsPurchesedService import MovieRegionTicketsPurchesedService
from src.infradata.Repositories.MovieRegionTicketsPurchesedRepository import MovieRegionTicketsPurchesedRepository
from src.application.Services.MovieService import MovieService
from src.infradata.Repositories.MovieRepository import MovieRepository
from src.application.Services.MovieTheaterService import MovieTheaterService
from src.infradata.Repositories.MovieTheaterRepository import MovieTheaterRepository
from src.application.Services.RegionService import RegionService
from src.infradata.Repositories.RegionRepository import RegionRepository


def movie_controller_injection() -> IMovieController:
    movie_region_tickets_purchesed_repository = MovieRegionTicketsPurchesedRepository()
    movie_region_tickets_purchesed_service = MovieRegionTicketsPurchesedService(
        movie_region_tickets_purchesed_repository)
    movie_repository = MovieRepository()
    region_repository = RegionRepository()
    region_service = RegionService(region_repository)
    cloudinary_uti = CloudinaryUti()

    movie_theater_repository = MovieTheaterRepository()
    movie_theater_service = MovieTheaterService(movie_theater_repository)

    movie_service = MovieService(
        movie_repository, movie_theater_service, region_service, movie_region_tickets_purchesed_service, cloudinary_uti)
    movie_validate = MovieValidate()

    controller = MovieController(movie_service, movie_validate)
    return controller
