from src.api.Validators.Interfaces.IMovieCreateValidate import IMovieCreateValidate
from src.application.Services.ResponseWrapper import ResponseWrapper
from cerberus import Validator


class MovieCreateValidate(IMovieCreateValidate):

    def movie_create_validate(cls, body: any) -> ResponseWrapper:
        body_validator = Validator({
            "title": {"type": "string", 'minlength': 3, "required": True, "empty": False},
            "description": {"type": "string", 'minlength': 3, "required": True, "empty": False},
            "gender": {"type": "string",  'minlength': 3, "required": True, "empty": False},
            "duration": {"type": "string", "required": True, "empty": False},
            "movieRating": {"type": "integer", "required": True, "empty": False},
            "base64Img": {"type": "string", "required": True, "empty": False},
            "statusMovie": {"type": "string", "required": True, "empty": True},
            "imgUrl": {"type": "string", "required": False, "empty": True},
            "publicId": {"type": "string", "required": False, "empty": True},
            "imgUrlBackground": {"type": "string", "required": False, "empty": True},
            "publicIdImgBackgound": {"type": "string", "required": False, "empty": True},
        })

        response = body_validator.validate(body)
        if response is False:
            return ResponseWrapper.fail(body_validator.errors)
        else:
            return ResponseWrapper.ok("tudo certo")
