from src.api.Validators.Interfaces.IMovieRegionTicketsPurchesedValidate import IMovieRegionTicketsPurchesedValidate
from src.application.Services.ResponseWrapper import ResponseWrapper
from cerberus import Validator


class MovieRegionTicketsPurchesedValidate(IMovieRegionTicketsPurchesedValidate):

    def movie_region_create_validate(cls, body: any) -> ResponseWrapper:
        body_validator = Validator({
            "movieId": {"type": "string", 'minlength': 36, "required": True, "empty": False},
            "cinemaId": {"type": "string", 'minlength': 36, "required": True, "empty": False},
            "ticketsSeats": {"type": "string", "required": True, "empty": False}

        })

        response = body_validator.validate(body)
        if response is False:
            return ResponseWrapper.fail(body_validator.errors)
        else:
            return ResponseWrapper.ok("tudo certo")

    def movie_region_update_validate(cls, body: any) -> ResponseWrapper:
        body_validator = Validator({
            "movieId": {"type": "string", 'minlength': 36, "required": True, "empty": False},
            "cinemaId": {"type": "string", 'minlength': 36, "required": True, "empty": False},
            "ticketsSeats": {"type": "string", "required": True, "empty": False}

        })

        response = body_validator.validate(body)
        if response is False:
            return ResponseWrapper.fail(body_validator.errors)
        else:
            return ResponseWrapper.ok("tudo certo")
