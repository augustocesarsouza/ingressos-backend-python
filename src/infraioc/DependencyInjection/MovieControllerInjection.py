from src.api.Controllers.MovieController import MovieController
from src.api.ControllersInterface.IMovieController import IMovieController
from src.api.Validators.MovieValidate import MovieValidate
from src.application.Services.AdditionalFoodMovieService import AdditionalFoodMovieService
from src.application.Services.CinemaMovieService import CinemaMovieService
from src.application.Services.CinemaService import CinemaService
from src.application.Services.FormOfPaymentService import FormOfPaymentService
from src.infradata.Repositories.AdditionalFoodMovieRepository import AdditionalFoodMovieRepository
from src.infradata.Repositories.CinemaRepository import CinemaRepository
from src.infradata.Repositories.CinemaMovieRepository import CinemaMovieRepository
from src.infradata.Repositories.FormOfPaymentRepository import FormOfPaymentRepository
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

    form_of_payment_repository = FormOfPaymentRepository()
    form_of_payment_service = FormOfPaymentService(form_of_payment_repository)

    cinema_movie_repository = CinemaMovieRepository()
    cinema_repository = CinemaRepository()
    cinema_service = CinemaService(cinema_repository)

    additional_food_movie_repository = AdditionalFoodMovieRepository()
    additional_food_movie_service = AdditionalFoodMovieService(
        additional_food_movie_repository, cloudinary_uti)

    cinema_movie_service = CinemaMovieService(
        cinema_movie_repository, region_service, cinema_service, None)

    movie_service = MovieService(
        movie_repository, movie_theater_service, region_service, movie_region_tickets_purchesed_service, form_of_payment_service, cinema_movie_service, additional_food_movie_service, cloudinary_uti)
    movie_validate = MovieValidate()

    controller = MovieController(movie_service, movie_validate)
    return controller
