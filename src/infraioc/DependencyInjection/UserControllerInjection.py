from src.api.Controllers.UserController import UserController
from src.api.ControllersInterface.IUserController import IUserController
from src.api.Validators.UserCreateValidate import UserCreateValidate
from src.application.Services.AdditionalInfoUserService import AdditionalInfoUserService
from src.application.Services.UserConfirmationService import UserConfirmationService
from src.application.Services.UserPermissionService import UserPermissionService
from src.infradata.Authentication.TokenGeneratorEmail import TokenGeneratorEmail
from src.infradata.Repositories.AdditionalInfoUserRepository import AdditionalInfoUserRepository
from src.infradata.Repositories.UserPermissionRepository import UserPermissionRepository
from src.infradata.Repositories.UserRepository import UserRepository
from src.application.Services.UserManagementService import UserManagementService
from src.application.Services.UserAuthenticationService import UserAuthenticationService
from src.infradata.SendEmailUser.SendEmailUser import SendEmailUser
from src.infradata.UtilityExternal.CacheRedisUti import CacheRedisUti
from src.infradata.UtilityExternal.SendEmailBrevo import SendEmailBrevo


def user_menagement_controller_injection() -> IUserController:
    # def __init__(self, cache_redis: ICacheRedisUti, send_email_brevo: ISendEmailBrevo) -> None:
    repository = UserRepository()
    cache_redis = CacheRedisUti()
    send_email_brevo = SendEmailBrevo()
    send_email_user = SendEmailUser(cache_redis, send_email_brevo)
    send_email_user = SendEmailUser(cache_redis, send_email_brevo)
    additional_info_user_repository = AdditionalInfoUserRepository()
    additional_info_user_service = AdditionalInfoUserService(
        additional_info_user_repository, repository)
    user_service = UserManagementService(
        repository, send_email_user, additional_info_user_service)

    user_permission_repository = UserPermissionRepository()
    user_permission_service = UserPermissionService(user_permission_repository)
    token_generator_email = TokenGeneratorEmail()
    user_authentication_service = UserAuthenticationService(
        repository, user_permission_service, token_generator_email, send_email_user)

    userConfirmationService = UserConfirmationService(repository, cache_redis)
    user_create_validate = UserCreateValidate()

    controller = UserController(
        user_service, user_authentication_service, userConfirmationService, user_create_validate)
    return controller


# def user_authentication_controller_injection() -> IUserController:
#     repository = UserRepository()
#     user_authentication_service = UserAuthenticationService(repository)
#     controller = UserController(None, user_authentication_service)
#     return controller
