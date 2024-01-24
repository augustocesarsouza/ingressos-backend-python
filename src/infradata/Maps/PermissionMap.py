from src.infradata.Context.Base import Base
from sqlalchemy import Column, CHAR, NVARCHAR, INTEGER


class PermissionMap(Base):
    __tablename__ = "Permission"

    Id = Column(INTEGER, primary_key=True, autoincrement=True)
    VisualName = Column(NVARCHAR(70), nullable=False)
    PermissionName = Column(NVARCHAR(70), nullable=False)

    def to_dict(self):
        return {
            key: value for key, value in vars(self).items() if value is not None
        }
