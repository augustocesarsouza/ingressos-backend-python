from cerberus import Validator
from src.application.Services.ResponseWrapper import ResponseWrapper
from datetime import datetime


def custom_date_coercion(value):
    try:
        # Tenta converter a string de data para o formato desejado
        return datetime.strptime(value, "%d/%m/%Y")
    except ValueError:
        # Se a conversão falhar, retorna None ou levanta uma exceção, dependendo da sua lógica
        return None


def user_update_validate(body: any):

    body_validator = Validator({
        "userId": {"type": "string", 'minlength': 36, "required": True, "empty": False},
        "birthDateString": {"type": "datetime", "required": True, "empty": True, "coerce": custom_date_coercion},
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
