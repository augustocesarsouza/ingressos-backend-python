from src.infradata.Context.Base import Base
from sqlalchemy import Column, CHAR, INTEGER, NVARCHAR, ForeignKey


class MovieTheaterMap(Base):
    __tablename__ = "MovieTheater"

    Id = Column(CHAR(36), primary_key=True, autoincrement=True)
    MovieId = Column(CHAR(36), ForeignKey('Movie.Id'), nullable=False)
    RegionId = Column(CHAR(36), ForeignKey('Region.Id'), nullable=False)

    def to_dict(self):
        return {
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }
