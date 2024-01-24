from src.api.Controllers.UserController import UserController
from src.api.ControllersInterface.IUserController import IUserController
from src.application.Services.UserConfirmationService import UserConfirmationService
from src.application.Services.UserPermissionService import UserPermissionService
from src.infradata.Authentication.TokenGeneratorEmail import TokenGeneratorEmail
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
    user_service = UserManagementService(repository, send_email_user)

    user_permission_repository = UserPermissionRepository()
    user_permission_service = UserPermissionService(user_permission_repository)
    token_generator_email = TokenGeneratorEmail()
    user_authentication_service = UserAuthenticationService(
        repository, user_permission_service, token_generator_email, send_email_user)

    userConfirmationService = UserConfirmationService(repository, cache_redis)

    controller = UserController(
        user_service, user_authentication_service, userConfirmationService)
    return controller


# def user_authentication_controller_injection() -> IUserController:
#     repository = UserRepository()
#     user_authentication_service = UserAuthenticationService(repository)
#     controller = UserController(None, user_authentication_service)
#     return controller