from src.infradata.Context.Base import Base
from sqlalchemy import Column, CHAR, NVARCHAR


class CinemaMap(Base):
    __tablename__ = "Cinema"

    Id = Column(CHAR(36), primary_key=True, autoincrement=False)
    NameCinema = Column(NVARCHAR(120), nullable=False)
    District = Column(NVARCHAR(120), nullable=False)
    Ranking = Column(NVARCHAR(100), nullable=False)

    def to_dict(self):
        return {
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }

    def set_attributes(self, id: str, name_cinema: str, district: str, ranking: str):
        self.Id = id
        self.NameCinema = name_cinema
        self.District = district
        self.Ranking = ranking
