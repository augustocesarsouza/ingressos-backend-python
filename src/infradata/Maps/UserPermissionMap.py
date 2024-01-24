from src.infradata.Context.Base import Base
from sqlalchemy import Column, CHAR, INTEGER, ForeignKey


class UserPermissionMap(Base):
    __tablename__ = "UserPermission"

    Id = Column(INTEGER, primary_key=True, autoincrement=True)
    UserId = Column(CHAR(36), ForeignKey("User.Id"), nullable=False)
    PermissionId = Column(INTEGER, ForeignKey("Permission.Id"), nullable=False)

    # user = relationship("User", back_populates="user_permission")
    # permission = relationship("Permission")

    def to_dict(self):
        return {
            key: value for key, value in vars(self).items() if value is not None
        }
