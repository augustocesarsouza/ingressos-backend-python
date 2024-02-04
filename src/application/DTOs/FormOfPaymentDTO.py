class FormOfPaymentDTO:
    def __init__(self, id: str, formName: str, price: str, movieId: str) -> None:
        self.Id = id
        self.FormName = formName
        self.Price = price
        self.MovieId = movieId

    def to_dict(self):
        return {
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }

    def set_id(self, guid_id: str):
        self.Id = guid_id
