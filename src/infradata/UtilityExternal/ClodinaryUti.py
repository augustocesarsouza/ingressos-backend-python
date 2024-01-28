from src.application.Services.ResponseWrapper import ResponseWrapper
from src.infradata.CloudinaryConfig.CloudinaryCreate import CloudinaryCreate
from src.infradata.UtilityExternal.Interface.IClodinaryUti import IClodinaryUti
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import cloudinary
from cloudinary import exceptions
from src.infradata.Config.JwtConfigFile import jwt_config
import base64


class ClodinaryUti(IClodinaryUti):

    def create_img(self, base_64: str, width: int, height: int) -> ResponseWrapper:

        try:
            cloudinary.config(
                cloud_name=jwt_config["CLOUD-NAME"],
                api_key=jwt_config["API-KEY"],
                api_secret=jwt_config["API-SECRET"],
                secure=True
            )

            print(type(base_64))

            upload_result = upload(
                str(base_64),
                transformation={
                    'width': width,
                    'height': height,
                    'crop': 'fill',
                    'quality': 100
                }
            )

            public_id = upload_result['public_id']
            image_url, options = cloudinary_url(
                public_id, width=width, height=height, crop="fill"
            )

            cloudinary_create = CloudinaryCreate(
                public_id, image_url)

            # print(cloudinary_create)

            return ResponseWrapper.ok(cloudinary_create)
        except exceptions.Error as e:
            return ResponseWrapper.fail(f"Erro no Cloudinary: {e}")
        except Exception as ex:
            return ResponseWrapper.fail(f"Erro inesperado: {ex}")
