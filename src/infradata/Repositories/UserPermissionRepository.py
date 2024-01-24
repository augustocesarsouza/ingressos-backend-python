from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IUserPermissionRepository import IUserPermissionRepository
from src.infradata.Context.ApplicationDbContext import ApplicationDbContext
from sqlalchemy.exc import SQLAlchemyError
from src.infradata.Maps.PermissionMap import PermissionMap
from src.infradata.Maps.UserPermissionMap import UserPermissionMap


class UserPermissionRepository(IUserPermissionRepository):

    @classmethod
    def get_all_permission_user(cls, idUser: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                user_permissions = (
                    database.session
                    # .query(UserPermissionMap, PermissionMap) tem esse outro jeito
                    .query(UserPermissionMap)
                    .join(PermissionMap, UserPermissionMap.PermissionId == PermissionMap.Id)
                    .filter(UserPermissionMap.UserId == idUser)
                    # .filter(UserPermissionMap.PermissionId == PermissionMap.Id)
                    .with_entities(
                        UserPermissionMap.Id,
                        UserPermissionMap.UserId,
                        PermissionMap.VisualName,
                        PermissionMap.PermissionName
                    )
                    .all()
                )

                array = []

                for item in user_permissions:
                    obj = {
                        "Id": item[0],
                        "UserId": item[1],
                        "VisualName": item[2],
                        "PermissionName": item[3]
                    }
                    array.append(obj)

                database.session.commit()
                return ResponseWrapper.ok(array)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")
