from cerberus import Validator, errors
from src.api.Validators.Interfaces.IAdditionalInfoUserValidate import IAdditionalInfoUserValidate
from src.application.Services.ResponseWrapper import ResponseWrapper
from datetime import datetime


class AdditionalInfoUserValidate(IAdditionalInfoUserValidate):

    def user_update_validate(self, body: any):
        body_validator = Validator({
            "userId": {"type": "string", 'minlength': 36, "required": True, "empty": False},
            "birthDateString": {
                "type": "datetime",
                "required": True,
                "empty": True,
                "coerce": self.custom_date_coercion,
            },
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
            # print(body_validator.errors)
            my_change = {}
            for x in body_validator.errors:
                # print(x)  # campo
                # print(body_validator.errors[x][0])  # value error
                obj = {x: [body_validator.errors[x][0]]}
                if x == "birthDateString":
                    my_change.setdefault(x, []).append(
                        "O campo birthDateString deve ser no formato DD/MM/AAAA")
                else:
                    my_change.setdefault(x, []).append(
                        body_validator.errors[x][0])

            return ResponseWrapper.fail(my_change)
        else:
            return ResponseWrapper.ok("tudo certo")

    def custom_date_coercion(self, value):
        try:
            # Tenta converter a string de data para o formato desejado
            result = datetime.strptime(value, "%d/%m/%Y")
            return result
        except ValueError:
            # Se a conversão falhar, retorna None ou levanta uma exceção, dependendo da sua lógica
            return None
