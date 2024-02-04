from src.api.Controllers.FormOfPaymentController import FormOfPaymentController
from src.api.ControllersInterface.IFormOfPaymentController import IFormOfPaymentController
from src.application.Services.FormOfPaymentService import FormOfPaymentService
from src.api.Validators.FormOfPaymentValidate import FormOfPaymentValidate
from src.infradata.Repositories.FormOfPaymentRepository import FormOfPaymentRepository


def form_of_payment_controller_injection() -> IFormOfPaymentController:
    form_of_payment_repository = FormOfPaymentRepository()

    form_of_payment_service = FormOfPaymentService(form_of_payment_repository)
    form_of_payment_validate = FormOfPaymentValidate()

    controller = FormOfPaymentController(
        form_of_payment_service, form_of_payment_validate)
    return controller
