class CloudinaryCreate:
    def __init__(self, public_id: str, img_url: str) -> None:
        self.public_id = public_id
        self.img_url = img_url

    def to_dict(self):
        return {
            key.lower(): value for key, value in vars(self).items() if value is not None
        }
