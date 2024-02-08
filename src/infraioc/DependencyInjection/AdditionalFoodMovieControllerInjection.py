from src.api.Controllers.AdditionalFoodMovieController import AdditionalFoodMovieController
from src.api.ControllersInterface.IAdditionalFoodMovieController import IAdditionalFoodMovieController
from src.api.Validators.AdditionalFoodMovieValidate import AdditionalFoodMovieValidate
from src.application.Services.AdditionalFoodMovieService import AdditionalFoodMovieService
from src.infradata.Repositories.AdditionalFoodMovieRepository import AdditionalFoodMovieRepository
from src.infradata.UtilityExternal.CloudinaryUti import CloudinaryUti


def additional_food_movie_controller_injection() -> IAdditionalFoodMovieController:
    additional_food_movie_repository = AdditionalFoodMovieRepository()
    cloudinary_util = CloudinaryUti()

    additional_food_movie_service = AdditionalFoodMovieService(
        additional_food_movie_repository, cloudinary_util)
    additional_food_movie_validate = AdditionalFoodMovieValidate()

    controller = AdditionalFoodMovieController(
        additional_food_movie_service, additional_food_movie_validate)
    return controller
