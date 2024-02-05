from src.api.Controllers.CinemaMovieController import CinemaMovieController
from src.api.ControllersInterface.ICinemaMovieController import ICinemaMovieController
from src.application.Services.CinemaMovieService import CinemaMovieService
from src.api.Validators.CinemaMovieValidate import CinemaMovieValidate
from src.application.Services.CinemaService import CinemaService
from src.application.Services.FormOfPaymentService import FormOfPaymentService
from src.application.Services.MovieRegionTicketsPurchesedService import MovieRegionTicketsPurchesedService
from src.application.Services.MovieTheaterService import MovieTheaterService
from src.application.Services.MovieService import MovieService
from src.application.Services.RegionService import RegionService
from src.infradata.Repositories.FormOfPaymentRepository import FormOfPaymentRepository
from src.infradata.Repositories.MovieRegionTicketsPurchesedRepository import MovieRegionTicketsPurchesedRepository
from src.infradata.Repositories.RegionRepository import RegionRepository
from src.infradata.Repositories.CinemaMovieRepository import CinemaMovieRepository
from src.infradata.Repositories.CinemaRepository import CinemaRepository
from src.infradata.Repositories.MovieRepository import MovieRepository
from src.infradata.Repositories.MovieTheaterRepository import MovieTheaterRepository
from src.infradata.UtilityExternal.CloudinaryUti import CloudinaryUti


def cinema_movie_controller_injection() -> ICinemaMovieController:
    movie_theater_repository = MovieTheaterRepository()
    region_repository = RegionRepository()
    cinema_repository = CinemaRepository()

    movie_repository = MovieRepository()
    movie_theater_service = MovieTheaterService(movie_theater_repository)
    cloudinary_util = CloudinaryUti()

    cinema_movie_repository = CinemaMovieRepository()
    region_service = RegionService(region_repository)
    cinema_service = CinemaService(cinema_repository)

    movie_region_tickets_purchesed_repository = MovieRegionTicketsPurchesedRepository()
    movie_region_tickets_purchesed_service = MovieRegionTicketsPurchesedService(
        movie_region_tickets_purchesed_repository)

    form_of_payment_repository = FormOfPaymentRepository()
    form_of_payment_service = FormOfPaymentService(form_of_payment_repository)

    cinema_movie_service2 = CinemaMovieService(
        cinema_movie_repository, region_service, cinema_service, None)

    movie_service = MovieService(
        movie_repository, movie_theater_service, region_service, movie_region_tickets_purchesed_service, form_of_payment_service, cinema_movie_service2, cloudinary_util)

    cinema_movie_service = CinemaMovieService(
        cinema_movie_repository, region_service, cinema_service, movie_service)
    cinema_movie_validate = CinemaMovieValidate()

    controller = CinemaMovieController(
        cinema_movie_service, cinema_movie_validate)
    return controller
