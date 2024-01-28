from src.infradata.Context.Base import Base
from sqlalchemy import Column, CHAR, NVARCHAR, INTEGER, DATETIME, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship


class TheatreMap(Base):
    __tablename__ = "Theatre"

    Id = Column(CHAR(36), primary_key=True, autoincrement=False)
    Title = Column(NVARCHAR(100), nullable=False)
    Description = Column(NVARCHAR(1000), nullable=False)
    Data = Column(DATETIME, nullable=False)
    Location = Column(NVARCHAR(100), nullable=False)
    TypeOfAttraction = Column(NVARCHAR(70), nullable=False)
    Category = Column(NVARCHAR(70), nullable=False)
    PublicId = Column(NVARCHAR(70), nullable=False)
    ImgUrl = Column(NVARCHAR(100), nullable=False)

    # user_permission = relationship("UserPermission", back_populates="user")

    def to_dict(self):
        return {
            key.lower(): value for key, value in vars(self).items() if value is not None
        }
