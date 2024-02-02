from src.application.DTOs.CinemaDTO import CinemaDTO
from src.infradata.Context.Base import Base
from sqlalchemy import Column, CHAR, NVARCHAR, ForeignKey
from sqlalchemy.orm import relationship


class CinemaMovieMap(Base):
    __tablename__ = "CinemaMovie"

    Id = Column(CHAR(36), primary_key=True, autoincrement=False)
    CinemaId = Column(CHAR(36), ForeignKey('Cinema.Id'), nullable=False)
    Cinema = CinemaDTO
    MovieId = Column(CHAR(36), ForeignKey('Movie.Id'), nullable=False)
    RegionId = Column(CHAR(36), ForeignKey('Region.Id'), nullable=False)
    ScreeningSchedule = Column(NVARCHAR(30), nullable=False)

    # user_permission = relationship("UserPermission", back_populates="user")

    def to_dict(self):
        return {
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }

    def set_attributes(self, id, cinema_id, movie_id, region_id, screening_schedule, cinema_dto: CinemaDTO):
        self.Id = id
        self.CinemaId = cinema_id
        self.MovieId = movie_id
        self.RegionId = region_id
        self.ScreeningSchedule = screening_schedule
        self.Cinema = cinema_dto
