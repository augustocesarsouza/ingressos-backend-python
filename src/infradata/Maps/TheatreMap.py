from src.application.DTOs.TheatreDTO import TheatreDTO
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
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }

    def insert_value_attribute(self, theatre_dto: TheatreDTO):
        self.Id = theatre_dto.Id
        self.Title = theatre_dto.Title
        self.Description = theatre_dto.Description
        self.Data = theatre_dto.Data
        self.Location = theatre_dto.Location
        self.TypeOfAttraction = theatre_dto.TypeOfAttraction
        self.Category = theatre_dto.Category
        self.PublicId = theatre_dto.PublicId
        self.ImgUrl = theatre_dto.ImgUrl
