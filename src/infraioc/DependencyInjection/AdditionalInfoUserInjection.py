from src.api.Controllers.AdditionalInfoUserController import AdditionalInfoUserController
from src.api.ControllersInterface.IAdditionalInfoUserController import IAdditionalInfoUserController
from src.application.Services.AdditionalInfoUserService import AdditionalInfoUserService
from src.infradata.Repositories.AdditionalInfoUserRepository import AdditionalInfoUserRepository
from src.infradata.Repositories.UserRepository import UserRepository


def user_additional_info_user_controller_injection() -> IAdditionalInfoUserController:
    additional_info_user_repository = AdditionalInfoUserRepository()
    user_repository = UserRepository()
    additional_info_user_service = AdditionalInfoUserService(
        additional_info_user_repository, user_repository)

    controller = AdditionalInfoUserController(additional_info_user_service)
    return controller
