from src.infradata.Context.Base import Base
from sqlalchemy import Column, CHAR, INTEGER, NVARCHAR, ForeignKey, DATETIME


class AdditionalInfoUserMap(Base):
    __tablename__ = "AdditionalInfoUser"

    Id = Column(INTEGER, primary_key=True, autoincrement=True)
    UserId = Column(CHAR(36), ForeignKey('User.Id'), nullable=False)
    BirthDate = Column(DATETIME, nullable=True)
    Gender = Column(NVARCHAR(50), nullable=True)
    Phone = Column(NVARCHAR(88), nullable=True)
    Cep = Column(NVARCHAR(40), nullable=True)
    Logradouro = Column(NVARCHAR(60), nullable=True)
    Numero = Column(NVARCHAR(30), nullable=True)
    Complemento = Column(NVARCHAR(40), nullable=True)
    Referencia = Column(NVARCHAR(40), nullable=True)
    Bairro = Column(NVARCHAR(50), nullable=True)
    Estado = Column(NVARCHAR(20), nullable=True)
    Cidade = Column(NVARCHAR(60), nullable=True)

    def to_dict(self):
        return {
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }
