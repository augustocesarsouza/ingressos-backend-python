from src.application.Services.Interfaces.IUserPermissionService import IUserPermissionService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IUserPermissionRepository import IUserPermissionRepository


class UserPermissionService(IUserPermissionService):
    def __init__(self, user_permission_repository: IUserPermissionRepository) -> None:
        self.__user_permission_repository = user_permission_repository

    def get_all_permission_user(self, idUser: str) -> ResponseWrapper:
        resultPermission = self.__user_permission_repository.get_all_permission_user(
            idUser)

        if resultPermission.Data == None or len(resultPermission.Data) <= 0:
            return ResponseWrapper.fail("we did not find permission for the user")

        if not resultPermission.IsSuccess:
            return resultPermission

        return resultPermission
