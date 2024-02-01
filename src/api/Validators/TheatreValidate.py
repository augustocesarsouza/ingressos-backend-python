from datetime import datetime
from src.api.Validators.Interfaces.ITheatreValidate import ITheatreValidate
from src.application.Services.ResponseWrapper import ResponseWrapper
from cerberus import Validator


class TheatreValidate(ITheatreValidate):

    def theatre_create_validate(self, body: any) -> ResponseWrapper:
        body_validator = Validator({
            "title": {"type": "string", 'minlength': 3, "required": True, "empty": False},
            "description": {"type": "string", 'minlength': 3, "required": True, "empty": False},
            "location": {"type": "string",  'minlength': 3, "required": True, "empty": False},
            "typeOfAttraction": {"type": "string", 'minlength': 3, "required": True, "empty": False},
            "category": {"type": "string", "required": True, "empty": False},
            "base64Img": {"type": "string", "required": True, "empty": False},
            "dataString": {"type": "datetime", "required": True, "empty": False, "coerce": self.custom_date_coercion},
        })

        response = body_validator.validate(body)
        if response is False:
            my_change = {}
            for x in body_validator.errors:
                # print(x)  # campo
                # print(body_validator.errors[x][0])  # value error
                if x == "dataString":
                    my_change.setdefault(x, []).append(
                        "O campo dataString deve ser no formato DD/MM/AAAA HH:MM")
                else:
                    my_change.setdefault(x, []).append(
                        body_validator.errors[x][0])

            return ResponseWrapper.fail(my_change)
        else:
            return ResponseWrapper.ok("tudo certo")

    def custom_date_coercion(self, value: str):
        date_hour_minute = value.split(" ")

        hour_minute = date_hour_minute[1]
        if len(hour_minute) < 5:
            return False

        try:
            # Tenta converter a string de data para o formato desejado
            result = datetime.strptime(value, "%d/%m/%Y %H:%M")
            print(result)
            return result
        except ValueError:
            # Se a conversão falhar, retorna None ou levanta uma exceção, dependendo da sua lógica

            return None

    def theatre_update_img_validate(self, body: any) -> ResponseWrapper:
        body_validator = Validator({
            "id": {"type": "string", 'minlength': 36, "required": True, "empty": False},
            "base64Img": {"type": "string", 'minlength': 3, "required": True, "empty": False}
        })

        response = body_validator.validate(body)
        if response is False:
            return ResponseWrapper.fail(response)
        else:
            return ResponseWrapper.ok("tudo certo")
