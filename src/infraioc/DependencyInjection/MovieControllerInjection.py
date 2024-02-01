from src.api.Controllers.MovieController import MovieController
from src.api.ControllersInterface.IMovieController import IMovieController
from src.api.Validators.MovieValidate import MovieValidate
from src.application.Services.MovieService import MovieService
from src.application.Services.MovieTheaterService import MovieTheaterService
from src.application.Services.RegionService import RegionService
from src.infradata.Repositories.MovieRepository import MovieRepository
from src.infradata.Repositories.MovieTheaterRepository import MovieTheaterRepository
from src.infradata.Repositories.RegionRepository import RegionRepository
from src.infradata.UtilityExternal.CloudinaryUti import CloudinaryUti


def movie_controller_injection() -> IMovieController:
    movie_repository = MovieRepository()
    region_repository = RegionRepository()
    region_service = RegionService(region_repository)
    cloudinary_uti = CloudinaryUti()

    movie_theater_repository = MovieTheaterRepository()
    movie_theater_service = MovieTheaterService(movie_theater_repository)

    movie_service = MovieService(
        movie_repository, movie_theater_service, region_service, cloudinary_uti)
    movie_validate = MovieValidate()

    controller = MovieController(movie_service, movie_validate)
    return controller
