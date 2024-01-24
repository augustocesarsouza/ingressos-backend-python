from src.infradata.Context.Base import Base
from sqlalchemy import Column, CHAR, NVARCHAR, INTEGER, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship


class UserMap(Base):
    __tablename__ = "User"

    Id = Column(CHAR(36), primary_key=True, autoincrement=False)
    Name = Column(NVARCHAR(100), nullable=False)
    Email = Column(NVARCHAR(100), nullable=False)
    Cpf = Column(NVARCHAR(85), nullable=True)
    PasswordHash = Column(NVARCHAR(255), nullable=False)
    ConfirmEmail = Column(INTEGER, nullable=True)

    # user_permission = relationship("UserPermission", back_populates="user")

    def to_dict(self):
        return {
            key.lower(): value for key, value in vars(self).items() if value is not None
        }

    def confirmed_email(self, value: int):
        self.ConfirmEmail = value
