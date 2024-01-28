from src.api.ControllersInterface.IMovieController import IMovieController
from src.api.HttpTypes.HttpRequest import HttpRequest
from src.api.HttpTypes.HttpResponse import HttpResponse
from src.api.Validators.Interfaces.IMovieCreateValidate import IMovieCreateValidate
from src.application.DTOs.MovieDTO import MovieDTO
from src.application.Services.Interfaces.IMovieService import IMovieService


class MovieController(IMovieController):
    def __init__(self, movie_service: IMovieService, movie_create_validate: IMovieCreateValidate) -> None:
        self.__movie_service = movie_service
        self.__movie_create_validate = movie_create_validate

    def get_all_movie_by_region_id(self, http_request: HttpRequest) -> HttpResponse:
        pass

    def get_info_movies_by_id(self, http_request: HttpRequest) -> HttpResponse:
        pass

    def get_status_movie(self, http_request: HttpRequest) -> HttpResponse:
        pass

    def create(self, http_request: HttpRequest) -> HttpResponse:
        result_valid_body = self.__movie_create_validate.movie_create_validate(
            http_request.body)

        if not result_valid_body.IsSuccess:
            return HttpResponse(
                status_code=422,
                body={"data": result_valid_body.Data}
            )

        title = http_request.body["title"]
        description = http_request.body["description"]
        gender = http_request.body["gender"]
        duration = http_request.body["duration"]
        statusMovie = http_request.body['statusMovie']
        base64Img = http_request.body['base64Img']
        movieRating = http_request.body['movieRating']

        movie_DTO = MovieDTO(id=None, title=title, description=description, gender=gender, duration=duration, movieRating=movieRating, imgUrl=None, publicId=None,
                             imgUrlBackground=None, publicIdImgBackgound=None, statusMovie=statusMovie, base_64_img=base64Img)

        result_create = self.__movie_service.create(movie_DTO)

        if result_create.IsSuccess:
            return HttpResponse(
                status_code=200,
                body={"data": result_create.Data}
            )
        else:
            return HttpResponse(
                status_code=400,
                body={"data": result_create.Data}
            )

    def delete_movie(self, http_request: HttpRequest) -> HttpResponse:
        id_movie = http_request.path_params["idMovie"]

        delete_movie_result = self.__movie_service.delete_movie(id_movie)

        if delete_movie_result.IsSuccess:
            return HttpResponse(
                status_code=200,
                body={"data": delete_movie_result.Data}
            )
        else:
            return HttpResponse(
                status_code=400,
                body={"data": delete_movie_result.Data}
            )

    def update_movie(self, http_request: HttpRequest) -> HttpResponse:
        pass

    def update_movie_img_background(self, http_request: HttpRequest) -> HttpResponse:
        pass
