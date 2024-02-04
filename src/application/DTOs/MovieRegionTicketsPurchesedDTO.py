from src.application.DTOs.CinemaDTO import CinemaDTO
from src.application.DTOs.MovieDTO import MovieDTO


class MovieRegionTicketsPurchesedDTO:
    def __init__(self, id: str, ticketsSeats: str, movieId: str, movieDTO: MovieDTO, cinemaId: str, cinemaDTO: CinemaDTO) -> None:
        self.Id = id
        self.TicketsSeats = ticketsSeats
        self.MovieId = movieId
        self.MovieDTO = movieDTO
        self.CinemaId = cinemaId
        self.CinemaDTO = cinemaDTO

    def to_dict(self):
        return {
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }

    def set_id(self, guid_id: str):
        self.Id = guid_id

    def tickets_seats_value(self, tickets_seats: str, tickets_seats_bank: str):
        if len(tickets_seats_bank) <= 0:
            self.TicketsSeats = tickets_seats
        elif len(tickets_seats) <= 0:
            self.TicketsSeats = tickets_seats
        elif len(tickets_seats_bank) > 0:
            string_join = f"{tickets_seats_bank},{tickets_seats}"
            self.TicketsSeats = string_join
