from src.infradata.Context.Base import Base
from sqlalchemy import Column, CHAR, NVARCHAR, INTEGER, DATETIME, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship


class RegionMap(Base):
    __tablename__ = "Region"

    Id = Column(CHAR(36), primary_key=True, autoincrement=False)
    State = Column(NVARCHAR(70), nullable=False)
    City = Column(NVARCHAR(70), nullable=False)

    # user_permission = relationship("UserPermission", back_populates="user")

    def to_dict(self):
        return {
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }
