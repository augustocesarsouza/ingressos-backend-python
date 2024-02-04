from src.application.DTOs.CinemaDTO import CinemaDTO
from src.application.DTOs.MovieDTO import MovieDTO
from src.infradata.Context.Base import Base
from sqlalchemy import Column, CHAR, NVARCHAR, ForeignKey
from sqlalchemy.orm import relationship


class MovieRegionTicketsPurchesedMap(Base):
    __tablename__ = "MovieRegionTicketsPurchesed"

    Id = Column(CHAR(36), primary_key=True, autoincrement=False)
    TicketsSeats = Column(NVARCHAR(200), nullable=False)
    MovieId = Column(CHAR(36), ForeignKey('Movie.Id'), nullable=False)
    MovieDTO = MovieDTO
    CinemaId = Column(CHAR(36), ForeignKey('Cinema.Id'), nullable=False)
    CinemaDTO = CinemaDTO

    # user_permission = relationship("UserPermission", back_populates="user")

    def to_dict(self):
        return {
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }
