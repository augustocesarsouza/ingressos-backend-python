from datetime import datetime


class TheatreDTO:
    def __init__(self, id: str, title: str, description: str, data: datetime, location: str, typeOfAttraction: str, category: str, imgUrl: str, publicId: str, base_64_img: str, dataString: str) -> None:
        self.Id = id
        self.Title = title
        self.Description = description
        self.Data = data
        self.Location = location
        self.TypeOfAttraction = typeOfAttraction
        self.Category = category
        self.ImgUrl = imgUrl
        self.PublicId = publicId
        self.Base64Img = base_64_img
        self.DataString = dataString

    def to_dict(self):
        return {
            key[0].lower() + key[1:]: value for key, value in vars(self).items() if value is not None
        }

    def add_imgUrl_PublicId(self, img_url: str, public_id: str):
        self.ImgUrl = img_url
        self.PublicId = public_id

    def set_id(self, id: str):
        self.Id = id

    def set_date(self, data: datetime):
        self.Data = data
