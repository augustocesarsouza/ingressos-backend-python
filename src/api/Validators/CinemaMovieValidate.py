from src.api.Validators.Interfaces.ICinemaMovieValidate import ICinemaMovieValidate
from src.application.Services.ResponseWrapper import ResponseWrapper
from cerberus import Validator


class CinemaMovieValidate(ICinemaMovieValidate):

    def cinema_movie_create_validate(cls, body: any) -> ResponseWrapper:
        body_validator = Validator({
            "cinemaId": {"type": "string", 'minlength': 36, "required": True, "empty": False},
            "movieId": {"type": "string", 'minlength': 36, "required": True, "empty": False},
            "regionId": {"type": "string",  'minlength': 36, "required": True, "empty": False},
            "screeningSchedule": {"type": "string",  'minlength': 3, "required": True, "empty": False}
        })

        response = body_validator.validate(body)
        if response is False:
            return ResponseWrapper.fail(body_validator.errors)
        else:
            return ResponseWrapper.ok("tudo certo")
