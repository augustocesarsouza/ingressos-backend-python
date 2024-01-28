class Movie:
    def __init__(self, id: str, title: str, description: str, gender: str, duration: str, movieRating: int, imgUrl: str, publicId: str, imgUrlBackground: str, publicIdImgBackgound: str, statusMovie: str) -> None:
        self.__Id = id
        self.__Title = title
        self.__Description = description
        self.__Gender = gender
        self.__Duration = duration
        self.__MovieRating = movieRating
        self.__ImgUrl = imgUrl
        self.__PublicId = publicId
        self.__ImgUrlBackground = imgUrlBackground
        self.__PublicIdImgBackgound = publicIdImgBackgound
        self.__StatusMovie = statusMovie
