from src.application.DTOs.CinemaDTO import CinemaDTO


class CinemaMovieDTO:
    def __init__(self, id: str, cinemaId: str, movieId: str, regionId: str, screeningSchedule: str, cinemaDTO: CinemaDTO) -> None:
        self.Id = id
        self.CinemaId = cinemaId
        self.MovieId = movieId
        self.RegionId = regionId
        self.ScreeningSchedule = screeningSchedule
        self.Cinema = cinemaDTO

    def to_dict(self):
        return {
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }

    def set_id(self, guid_id: str):
        self.Id = guid_id
