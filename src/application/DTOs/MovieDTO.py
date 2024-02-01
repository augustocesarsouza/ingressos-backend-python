class MovieDTO:
    def __init__(self, id: str, title: str, description: str, gender: str, duration: str, movieRating: int, imgUrl: str, publicId: str, imgUrlBackground: str, publicIdImgBackgound: str, statusMovie: str, base_64_img: str) -> None:
        self.Id = id
        self.Title = title
        self.Description = description
        self.Gender = gender
        self.Duration = duration
        self.MovieRating = movieRating
        self.ImgUrl = imgUrl
        self.PublicId = publicId
        self.ImgUrlBackground = imgUrlBackground
        self.PublicIdImgBackgound = publicIdImgBackgound
        self.StatusMovie = statusMovie
        self.Base64Img = base_64_img

    def to_dict(self):
        return {
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }

    def add_imgUrl_PublicId_ImgUrlBackground_PublicIdImgBackgound(self, img_url: str, public_id: str, img_url_background: str, public_id_img_backgound: str):
        self.ImgUrl = img_url
        self.PublicId = public_id
        self.ImgUrlBackground = img_url_background
        self.PublicIdImgBackgound = public_id_img_backgound
