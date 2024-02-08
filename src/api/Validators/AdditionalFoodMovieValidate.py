from src.api.Validators.Interfaces.IAdditionalFoodMovieValidate import IAdditionalFoodMovieValidate
from src.application.Services.ResponseWrapper import ResponseWrapper
from cerberus import Validator


class AdditionalFoodMovieValidate(IAdditionalFoodMovieValidate):

    def additional_food_create_validate(self, body: any) -> ResponseWrapper:
        body_validator = Validator({
            "title": {"type": "string", "required": True, "empty": False},
            "price": {"type": "string", "required": True, "empty": False},
            "fee": {"type": "string", "required": True, "empty": False},
            "movieId": {"type": "string",  'minlength': 36, "required": True, "empty": False},
            "base64Img": {"type": "string",  'minlength': 3, "required": True, "empty": False}
        })

        response = body_validator.validate(body)
        if response is False:
            return ResponseWrapper.fail(body_validator.errors)
        else:
            return ResponseWrapper.ok("tudo certo")
