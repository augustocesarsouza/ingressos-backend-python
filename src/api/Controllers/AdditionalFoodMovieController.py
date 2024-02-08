from src.api.ControllersInterface.IAdditionalFoodMovieController import IAdditionalFoodMovieController
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.HttpTypes.HttpResponse import HttpResponse
from src.api.Validators.Interfaces.IAdditionalFoodMovieValidate import IAdditionalFoodMovieValidate
from src.application.DTOs.AdditionalFoodMovieDTO import AdditionalFoodMovieDTO
from src.application.Services.Interfaces.IAdditionalFoodMovieService import IAdditionalFoodMovieService


class AdditionalFoodMovieController(IAdditionalFoodMovieController):
    def __init__(self, additional_food_movie_service: IAdditionalFoodMovieService, additional_food_movie_validate: IAdditionalFoodMovieValidate) -> None:
        self.__additional_food_movie_service = additional_food_movie_service
        self.__additional_food_movie_validate = additional_food_movie_validate

    def get_all_food_movie(self, http_request: HttpRequest) -> HttpResponse:
        movie_id = http_request.path_params["movieId"]

        result_get_all_food = self.__additional_food_movie_service.get_all_food_movie(
            movie_id)

        if result_get_all_food.IsSuccess:
            return HttpResponse(
                status_code=200,
                body={"data": result_get_all_food.Data}
            )
        else:
            return HttpResponse(
                status_code=400,
                body={"data": result_get_all_food.Data}
            )

    def create(self, http_request: HttpRequest) -> HttpResponse:
        result_validate_body = self.__additional_food_movie_validate.additional_food_create_validate(
            http_request.body)

        if not result_validate_body.IsSuccess:
            return HttpResponse(
                status_code=422,
                body={"data": result_validate_body.Data}
            )

        title = http_request.body["title"]
        price = http_request.body["price"]
        fee = http_request.body["fee"]
        movie_id = http_request.body["movieId"]
        base64Img = http_request.body["base64Img"]

        additional_food_movie_dto = AdditionalFoodMovieDTO(id=None, title=title, price=price,
                                                           fee=fee, imgUrl=None, publicId=None, base64Img=base64Img, movieId=movie_id, movie=None)

        result_create_service = self.__additional_food_movie_service.create(
            additional_food_movie_dto)

        if result_create_service.IsSuccess:
            return HttpResponse(
                status_code=200,
                body={"data": result_create_service.Data}
            )
        else:
            return HttpResponse(
                status_code=400,
                body={"data": result_create_service.Data}
            )
    # fazer delete amanha para a class movieService delete de um movie
    # tem que deletar a imagem do cloudinary
