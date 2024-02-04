from src.infradata.Context.Base import Base
from sqlalchemy import Column, CHAR, NVARCHAR, ForeignKey


class FormOfPaymentMap(Base):
    __tablename__ = "FormOfPayment"

    Id = Column(CHAR(36), primary_key=True, autoincrement=False)
    FormName = Column(NVARCHAR(60), nullable=False)
    Price = Column(NVARCHAR(60), nullable=False)
    MovieId = Column(CHAR(36), ForeignKey('Movie.Id'), nullable=False)

    def to_dict(self):
        return {
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }
