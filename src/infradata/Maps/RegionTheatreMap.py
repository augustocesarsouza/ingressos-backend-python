from src.infradata.Context.Base import Base
from sqlalchemy import Column, CHAR, NVARCHAR, INTEGER, DATETIME, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship


class RegionTheatreMap(Base):
    __tablename__ = "RegionTheatre"

    Id = Column(CHAR(36), primary_key=True, autoincrement=True)
    TheatreId = Column(CHAR(36), ForeignKey('Theatre.Id'), nullable=False)
    RegionId = Column(CHAR(36), ForeignKey('Region.Id'), nullable=False)

    # user_permission = relationship("UserPermission", back_populates="user")

    def to_dict(self):
        return {
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }
