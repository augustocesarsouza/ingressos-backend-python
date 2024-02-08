from src.infradata.Context.Base import Base
from sqlalchemy import Column, CHAR, INTEGER, NVARCHAR, ForeignKey, DATETIME


class AdditionalFoodMovieMap(Base):
    __tablename__ = "AdditionalFoodMovie"

    Id = Column(CHAR(36), primary_key=True)
    Title = Column(NVARCHAR(100), nullable=False)
    Price = Column(NVARCHAR(60), nullable=False)
    Fee = Column(NVARCHAR(60), nullable=False)
    ImgUrl = Column(NVARCHAR(140), nullable=False)
    PublicId = Column(NVARCHAR(70), nullable=False)
    MovieId = Column(CHAR(36), ForeignKey('Movie.Id'), nullable=False)

    def to_dict(self):
        return {
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }
