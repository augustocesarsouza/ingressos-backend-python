from datetime import datetime


class AdditionalInfoUserDTO:
    def __init__(self, id: int, userId: str, birthDate: datetime, birthDateString: str, gender: str, phone: str, cep: str, logradouro: str, numero: str, complemento: str, referencia: str, bairro: str, estado: str, cidade: str) -> None:
        self.Id = id
        self.UserId = userId
        self.BirthDate = birthDate
        self.BirthDateString = birthDateString
        self.Gender = gender
        self.Phone = phone
        self.Cep = cep
        self.Logradouro = logradouro
        self.Numero = numero
        self.Complemento = complemento
        self.Referencia = referencia
        self.Bairro = bairro
        self.Estado = estado
        self.Cidade = cidade

    def to_dict(self):
        return {
            key.lower(): value for key, value in vars(self).items() if value is not None
        }

    def set_birth_date(self, birth_bate: datetime):
        self.BirthDate = birth_bate

    def set_user_id(self, user_id: str):
        self.UserId = user_id
