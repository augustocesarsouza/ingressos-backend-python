class User:
    def __init__(self, Id: str, Name: str, Email: str, Cpf: str, PasswordHash: str, ConfirmEmail: int) -> None:
        self.__Id = Id
        self.__Name = Name
        self.__Email = Email
        self.__PasswordHash = PasswordHash
        self.__ConfirmEmail = ConfirmEmail
