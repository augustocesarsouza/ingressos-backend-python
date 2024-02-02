class CinemaDTO:
    def __init__(self, id: str, nameCinema: str, district: str, ranking: str) -> None:
        self.Id = id
        self.NameCinema = nameCinema
        self.District = district
        self.Ranking = ranking

    def to_dict(self):
        return {
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }

    def set_id(self, guid_id: str):
        self.Id = guid_id
