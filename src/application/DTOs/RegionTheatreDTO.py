class RegionTheatreDTO:
    def __init__(self, id: str, theatreId: str, regionId: str) -> None:
        self.Id = id
        self.TheatreId = theatreId
        self.RegionId = regionId

    def to_dict(self):
        return {
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }
