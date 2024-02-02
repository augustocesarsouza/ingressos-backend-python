from src.api.Validators.Interfaces.ICinemaValidate import ICinemaValidate
from src.application.Services.ResponseWrapper import ResponseWrapper
from cerberus import Validator


class CinemaValidate(ICinemaValidate):

    def cinema_create_validate(cls, body: any) -> ResponseWrapper:
        body_validator = Validator({
            "nameCinema": {"type": "string", 'minlength': 3, "required": True, "empty": False},
            "district": {"type": "string", 'minlength': 3, "required": True, "empty": False},
            "ranking": {"type": "string",  'minlength': 3, "required": True, "empty": False}
        })

        response = body_validator.validate(body)
        if response is False:
            return ResponseWrapper.fail(body_validator.errors)
        else:
            return ResponseWrapper.ok("tudo certo")
