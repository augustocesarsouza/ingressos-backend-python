from cerberus import Validator
from src.application.Services.ResponseWrapper import ResponseWrapper


def user_create_validate(body: any):

    body_validator = Validator({
        "name": {"type": "string", 'minlength': 1, "required": True, "empty": False},
        "email": {"type": "string", "required": True, "empty": False},
        "cpf": {"type": "string",  'minlength': 11, "required": True, "empty": False},
        "password": {"type": "string", 'minlength': 12, "required": True, "empty": False}
    })

    response = body_validator.validate(body)
    if response is False:
        return ResponseWrapper.fail(body_validator.errors)
    else:
        return ResponseWrapper.ok("tudo certo")
