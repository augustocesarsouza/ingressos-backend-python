from src.api.Validators.Interfaces.IFormOfPaymentValidate import IFormOfPaymentValidate
from src.application.Services.ResponseWrapper import ResponseWrapper
from cerberus import Validator


class FormOfPaymentValidate(IFormOfPaymentValidate):

    def form_of_payment_create_validate(cls, body: any) -> ResponseWrapper:
        body_validator = Validator({
            "formName": {"type": "string", "required": True, "empty": False},
            "price": {"type": "string", "required": True, "empty": False},
            "movieId": {"type": "string",  'minlength': 36, "required": True, "empty": False}
        })

        response = body_validator.validate(body)
        if response is False:
            return ResponseWrapper.fail(body_validator.errors)
        else:
            return ResponseWrapper.ok("tudo certo")
