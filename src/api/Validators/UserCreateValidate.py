from cerberus import Validator
from src.api.Validators.Interfaces.IUserCreateValidate import IUserCreateValidate
from src.application.Services.ResponseWrapper import ResponseWrapper


class UserCreateValidate(IUserCreateValidate):

    def user_create_validate(cls, body: any) -> ResponseWrapper:
        body_validator = Validator({
            "name": {"type": "string", 'minlength': 1, "required": True, "empty": False},
            "email": {"type": "string", "required": True, "empty": False},
            "cpf": {"type": "string",  'minlength': 11, "required": True, "empty": False},
            "password": {"type": "string", 'minlength': 12, "required": True, "empty": False},
            "birthDateString": {"type": "string", "required": True, "empty": True},
            "gender": {"type": "string", "required": True, "empty": True},
            "phone": {"type": "string", "required": True, "empty": True},
            "cep": {"type": "string", "required": True, "empty": True},
            "logradouro": {"type": "string", "required": True, "empty": True},
            "numero": {"type": "string", "required": True, "empty": True},
            "complemento": {"type": "string", "required": True, "empty": True},
            "referencia": {"type": "string", "required": True, "empty": True},
            "bairro": {"type": "string", "required": True, "empty": True},
            "estado": {"type": "string", "required": True, "empty": True},
            "cidade": {"type": "string", "required": True, "empty": True}
        })

        response = body_validator.validate(body)
        if response is False:
            return ResponseWrapper.fail(body_validator.errors)
        else:
            return ResponseWrapper.ok("tudo certo")
