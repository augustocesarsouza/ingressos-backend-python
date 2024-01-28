from src.infradata.Context.Base import Base
from sqlalchemy import Column, CHAR, NVARCHAR, INTEGER, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship


class MovieMap(Base):
    __tablename__ = "Movie"

    Id = Column(CHAR(36), primary_key=True, autoincrement=False)
    Title = Column(NVARCHAR(100), nullable=False)
    Description = Column(NVARCHAR(1000), nullable=False)
    Gender = Column(NVARCHAR(50), nullable=False)
    Duration = Column(NVARCHAR(30), nullable=False)
    MovieRating = Column(INTEGER, nullable=False)
    ImgUrl = Column(NVARCHAR(100), nullable=False)
    PublicId = Column(NVARCHAR(70), nullable=False)
    ImgUrlBackground = Column(NVARCHAR(100), nullable=False)
    PublicIdImgBackgound = Column(NVARCHAR(70), nullable=True)
    StatusMovie = Column(NVARCHAR(30), nullable=False)

    # user_permission = relationship("UserPermission", back_populates="user")

    def to_dict(self):
        return {
            key.lower(): value for key, value in vars(self).items() if value is not None
        }
