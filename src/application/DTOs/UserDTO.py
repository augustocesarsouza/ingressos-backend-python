class UserDTO:
    def __init__(self, Id: str, Name: str, Email: str, Cpf: str, PasswordHash: str, ConfirmEmail: int, token: str) -> None:
        self.Id = Id
        self.Name = Name
        self.Email = Email
        self.Cpf = Cpf
        self.PasswordHash = PasswordHash
        self.ConfirmEmail = ConfirmEmail
        self.Token = token

    def to_dict(self):
        return {
            key.lower(): value for key, value in vars(self).items() if value is not None
        }
