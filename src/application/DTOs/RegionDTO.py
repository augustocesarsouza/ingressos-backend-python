class RegionDTO:
    def __init__(self, id: str, state: str, city: str) -> None:
        self.Id = id
        self.State = state
        self.City = city

    def to_dict(self):
        return {
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }
