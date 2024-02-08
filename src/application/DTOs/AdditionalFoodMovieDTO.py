from src.application.DTOs.MovieDTO import MovieDTO


class AdditionalFoodMovieDTO:
    def __init__(self, id: int, title: str, price: str, fee: str, imgUrl: str, publicId: str, base64Img: str, movieId: str, movie: MovieDTO = None) -> None:
        self.Id = id
        self.Title = title
        self.Price = price
        self.Fee = fee
        self.ImgUrl = imgUrl
        self.PublicId = publicId
        self.Base64Img = base64Img
        self.MovieId = movieId
        self.Movie = movie

    def to_dict(self):
        return {
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }

    def set_id(self, id: str):
        self.Id = id
