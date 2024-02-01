import unittest
from unittest.mock import Mock
from src.application.DTOs.MovieDTO import MovieDTO
from src.application.DTOs.RegionDTO import RegionDTO

from src.application.Services.MovieService import MovieService
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IMovieRepository import IMovieRepository
from src.application.Services.Interfaces.IRegionService import IRegionService
from src.infradata.CloudinaryConfig.CloudinaryCreate import CloudinaryCreate
from src.infradata.UtilityExternal.Interface.ICloudinaryUti import ICloudinaryUti
from src.application.Services.Interfaces.IMovieTheaterService import IMovieTheaterService


class MovieServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_movie_repository = Mock(spec=IMovieRepository)
        self.mock_movie_theater_service = Mock(spec=IMovieTheaterService)
        self.mock_region_service = Mock(spec=IRegionService)
        self.mock_cloudinary_uti = Mock(spec=ICloudinaryUti)

    # test func 'get_all_movie_by_region_id'
    def test_get_all_movie_by_region_id_without_error(self):
        region_dto = RegionDTO(
            "961b70f2-232f-4a10-930c-601064ab2cac", None, None)

        self.mock_region_service.get_id_by_name_state.return_value = ResponseWrapper.ok(
            region_dto)

        obj1 = {
            "id": "e92da0j8-0c10-24d1-88ab-b270c43183a0",
            "imgUrl": "imgUrl1",
            "movieRating": 16,
            "title": "Napoleão"
        }

        movie_all = []
        movie_all.append(obj1)

        self.mock_movie_repository.get_all_movie_by_region_id.return_value = ResponseWrapper.ok(
            movie_all)

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.get_all_movie_by_region_id("region")
        self.assertEqual(result.IsSuccess, True)

    def test_get_all_movie_by_region_id_with_error_get_id_by_name_state(self):
        self.mock_region_service.get_id_by_name_state.return_value = ResponseWrapper.fail(
            "error get region")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.get_all_movie_by_region_id("region")
        self.assertEqual(result.IsSuccess, False)

    def test_get_all_movie_by_region_id_with_error_all_movie_database(self):
        region_dto = RegionDTO(
            "961b70f2-232f-4a10-930c-601064ab2cac", None, None)

        self.mock_region_service.get_id_by_name_state.return_value = ResponseWrapper.ok(
            region_dto)

        self.mock_movie_repository.get_all_movie_by_region_id.return_value = ResponseWrapper.fail(
            "error get all movie, database error")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.get_all_movie_by_region_id("region")
        self.assertEqual(result.IsSuccess, False)

    def test_get_all_movie_by_region_id_with_error_movie_all_empty(self):
        region_dto = RegionDTO(
            "961b70f2-232f-4a10-930c-601064ab2cac", None, None)

        self.mock_region_service.get_id_by_name_state.return_value = ResponseWrapper.ok(
            region_dto)

        movie_all = []

        self.mock_movie_repository.get_all_movie_by_region_id.return_value = ResponseWrapper.ok(
            movie_all)

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.get_all_movie_by_region_id("region")
        self.assertEqual(result.IsSuccess, False)
        self.assertEqual(result.Data["message"], "we did not find movies")

    # test func 'get_info_movies_by_id'
    def test_get_info_movies_by_id_without_error(self):
        self.mock_movie_repository.get_info_movies_by_id.return_value = ResponseWrapper.ok(
            "Ok, found movie")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.get_info_movies_by_id(
            "961b70f2-232f-4a10-930c-601064ab2cac")
        self.assertEqual(result.IsSuccess, True)

    def test_get_info_movies_by_id_with_error_found_movie(self):
        self.mock_movie_repository.get_info_movies_by_id.return_value = ResponseWrapper.fail(
            "error, found movie")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.get_info_movies_by_id(
            "961b70f2-232f-4a10-930c-601064ab2cac")
        self.assertEqual(result.IsSuccess, False)

    # test func 'get_status_movie'
    def test_get_status_movie_without_error(self):
        self.mock_movie_repository.get_status_movie.return_value = ResponseWrapper.ok(
            "Ok, found movie, by statusMovie")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.get_status_movie("Highlight")
        self.assertEqual(result.IsSuccess, True)

    def test_get_status_movie_with_error_found_movie_status(self):
        self.mock_movie_repository.get_status_movie.return_value = ResponseWrapper.fail(
            "error, found movie, by statusMovie")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.get_status_movie("Highlight")
        self.assertEqual(result.IsSuccess, False)

    # test func 'create'
    def test_create_without_error(self):
        self.mock_cloudinary_uti.create_img.side_effect = [
            ResponseWrapper.ok(CloudinaryCreate("public_id1", "image_url1")),
            ResponseWrapper.ok(CloudinaryCreate("public_id2", "image_url2"))
        ]

        self.mock_movie_repository.create.return_value = ResponseWrapper.ok(
            "ok, create")

        movie_DTO = MovieDTO(id=None, title="title1", description="description1", gender="gender1", duration="duration1", movieRating="movieRating1", imgUrl=None, publicId=None,
                             imgUrlBackground=None, publicIdImgBackgound=None, statusMovie="statusMovie1", base_64_img="base64Img1")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.create(movie_DTO)
        self.assertEqual(result.IsSuccess, True)

    def test_create_with_error_movie_DTO_None(self):
        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.create(None)
        self.assertEqual(result.IsSuccess, False)

    def test_create_with_error_try_create_img1_cloudinary(self):
        self.mock_cloudinary_uti.create_img.return_value = ResponseWrapper.fail(
            "Error create first img1 cloudinary")

        movie_DTO = MovieDTO(id=None, title="title1", description="description1", gender="gender1", duration="duration1", movieRating="movieRating1", imgUrl=None, publicId=None,
                             imgUrlBackground=None, publicIdImgBackgound=None, statusMovie="statusMovie1", base_64_img="base64Img1")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.create(movie_DTO)
        self.assertEqual(result.IsSuccess, False)

    def test_create_with_error_try_create_img2_cloudinary(self):
        self.mock_cloudinary_uti.create_img.side_effect = [
            ResponseWrapper.ok(CloudinaryCreate("public_id1", "image_url1")),
            ResponseWrapper.fail("Error create second img2 cloudinary")
        ]

        movie_DTO = MovieDTO(id=None, title="title1", description="description1", gender="gender1", duration="duration1", movieRating="movieRating1", imgUrl=None, publicId=None,
                             imgUrlBackground=None, publicIdImgBackgound=None, statusMovie="statusMovie1", base_64_img="base64Img1")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.create(movie_DTO)
        self.assertEqual(result.IsSuccess, False)

    def test_create_without_error(self):
        self.mock_cloudinary_uti.create_img.side_effect = [
            ResponseWrapper.ok(CloudinaryCreate("public_id1", "image_url1")),
            ResponseWrapper.ok(CloudinaryCreate("public_id2", "image_url2"))
        ]

        self.mock_movie_repository.create.return_value = ResponseWrapper.fail(
            "error, create database")

        movie_DTO = MovieDTO(id=None, title="title1", description="description1", gender="gender1", duration="duration1", movieRating="movieRating1", imgUrl=None, publicId=None,
                             imgUrlBackground=None, publicIdImgBackgound=None, statusMovie="statusMovie1", base_64_img="base64Img1")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.create(movie_DTO)
        self.assertEqual(result.IsSuccess, False)

    # test func 'delete_movie'
    def test_delete_movie_without_error(self):
        self.mock_movie_repository.get_by_id.return_value = ResponseWrapper.ok(
            "ok, found movie")

        self.mock_movie_theater_service.delete.return_value = ResponseWrapper.ok(
            "ok, delete join")

        movie_DTO = MovieDTO(id=None, title=None, description=None, gender=None, duration=None, movieRating=None, imgUrl=None, publicId="publicId1",
                             imgUrlBackground=None, publicIdImgBackgound="publicIdImgBackgound1", statusMovie=None, base_64_img=None).to_dict()

        self.mock_movie_repository.delete.return_value = ResponseWrapper.ok(
            movie_DTO)

        self.mock_cloudinary_uti.delete_img.return_value = ResponseWrapper.ok(
            "deleted img main cloudinary")

        self.mock_cloudinary_uti.delete_img.return_value = ResponseWrapper.ok(
            "deleted img background cloudinary")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.delete_movie(
            "961b70f2-232f-4a10-930c-601064ab2cac")
        self.assertEqual(result.IsSuccess, True)

    def test_delete_movie_with_error_when_confirm_if_movie_exist(self):
        self.mock_movie_repository.get_by_id.return_value = ResponseWrapper.fail(
            None)

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.delete_movie(
            "961b70f2-232f-4a10-930c-601064ab2cac")
        self.assertEqual(result.IsSuccess, False)

    def test_delete_movie_with_error_get_movie_database_error(self):
        self.mock_movie_repository.get_by_id.return_value = ResponseWrapper.fail(
            "error database")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.delete_movie(
            "961b70f2-232f-4a10-930c-601064ab2cac")
        self.assertEqual(result.IsSuccess, False)

    def test_delete_movie_with_error_when_delete_join_movietheater(self):
        self.mock_movie_repository.get_by_id.return_value = ResponseWrapper.ok(
            "ok, found movie")

        self.mock_movie_theater_service.delete.return_value = ResponseWrapper.fail(
            "error")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.delete_movie(
            "961b70f2-232f-4a10-930c-601064ab2cac")
        self.assertEqual(result.IsSuccess, False)

    def test_delete_movie_with_error_when_delete_movie(self):
        self.mock_movie_repository.get_by_id.return_value = ResponseWrapper.ok(
            "ok, found movie")

        self.mock_movie_theater_service.delete.return_value = ResponseWrapper.ok(
            "ok, delete join")

        self.mock_movie_repository.delete.return_value = ResponseWrapper.fail(
            "error when delete movie")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.delete_movie(
            "961b70f2-232f-4a10-930c-601064ab2cac")
        self.assertEqual(result.IsSuccess, False)

    def test_delete_movie_error_when_delete_img_main(self):
        self.mock_movie_repository.get_by_id.return_value = ResponseWrapper.ok(
            "ok, found movie")

        self.mock_movie_theater_service.delete.return_value = ResponseWrapper.ok(
            "ok, delete join")

        movie_DTO = MovieDTO(id=None, title=None, description=None, gender=None, duration=None, movieRating=None, imgUrl=None, publicId="publicId1",
                             imgUrlBackground=None, publicIdImgBackgound="publicIdImgBackgound1", statusMovie=None, base_64_img=None).to_dict()

        self.mock_movie_repository.delete.return_value = ResponseWrapper.ok(
            movie_DTO)

        self.mock_cloudinary_uti.delete_img.return_value = ResponseWrapper.fail(
            "soma error occurred when delete img main")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.delete_movie(
            "961b70f2-232f-4a10-930c-601064ab2cac")
        self.assertEqual(result.IsSuccess, False)

    def test_delete_movie_error_when_delete_img_background(self):
        self.mock_movie_repository.get_by_id.return_value = ResponseWrapper.ok(
            "ok, found movie")

        self.mock_movie_theater_service.delete.return_value = ResponseWrapper.ok(
            "ok, delete join")

        movie_DTO = MovieDTO(id=None, title=None, description=None, gender=None, duration=None, movieRating=None, imgUrl=None, publicId="publicId1",
                             imgUrlBackground=None, publicIdImgBackgound="publicIdImgBackgound1", statusMovie=None, base_64_img=None).to_dict()

        self.mock_movie_repository.delete.return_value = ResponseWrapper.ok(
            movie_DTO)

        self.mock_cloudinary_uti.delete_img.return_value = ResponseWrapper.ok(
            "deleted img main cloudinary")

        self.mock_cloudinary_uti.delete_img.return_value = ResponseWrapper.fail(
            "soma error occurred when delete img background")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.delete_movie(
            "961b70f2-232f-4a10-930c-601064ab2cac")
        self.assertEqual(result.IsSuccess, False)

    # test func 'update_movie'
    def test_update_movie_without_error(self):
        movie_dto_database = MovieDTO(id=None, title=None, description=None, gender=None, duration=None, movieRating=None, imgUrl=None, publicId="publicId1",
                                      imgUrlBackground=None, publicIdImgBackgound="publicIdImgBackgound1", statusMovie=None, base_64_img=None)

        self.mock_movie_repository.get_by_id_only_publicId_PublicIdImgBackgound.return_value = ResponseWrapper.ok(
            movie_dto_database)

        self.mock_cloudinary_uti.delete_img.side_effect = [
            ResponseWrapper.ok("deleted img main cloudinary"),
            ResponseWrapper.ok("deleted img background cloudinary")
        ]

        self.mock_cloudinary_uti.create_img.side_effect = [
            ResponseWrapper.ok(CloudinaryCreate("public_id1", "image_url1")),
            ResponseWrapper.ok(CloudinaryCreate("public_id2", "image_url2"))
        ]

        self.mock_movie_repository.update_movie.return_value = ResponseWrapper.ok(
            "updated successfully")

        movie_DTO = MovieDTO(id="961b70f2-232f-4a10-930c-601064ab2cac", title=None, description=None, gender=None, duration=None, movieRating=None, imgUrl=None, publicId=None,
                             imgUrlBackground=None, publicIdImgBackgound=None, statusMovie=None, base_64_img="seila_base_64")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.update_movie(movie_DTO)
        self.assertEqual(result.IsSuccess, True)

    def test_update_movie_error_when_get_info_movie_for_delete_imgMain_and_imgBackground_not_exist_movie(self):
        self.mock_movie_repository.get_by_id_only_publicId_PublicIdImgBackgound.return_value = ResponseWrapper.ok(
            None)

        movie_DTO = MovieDTO(id="961b70f2-232f-4a10-930c-601064ab2cac", title=None, description=None, gender=None, duration=None, movieRating=None, imgUrl=None, publicId=None,
                             imgUrlBackground=None, publicIdImgBackgound=None, statusMovie=None, base_64_img="seila_base_64")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.update_movie(movie_DTO)
        self.assertEqual(result.IsSuccess, False)
        self.assertEqual(result.Data["message"], "not fould movie")

    def test_update_movie_error_when_get_info_movie_for_delete_imgMain_and_imgBackground_database(self):
        self.mock_movie_repository.get_by_id_only_publicId_PublicIdImgBackgound.return_value = ResponseWrapper.fail(
            "error when get database")

        movie_DTO = MovieDTO(id="961b70f2-232f-4a10-930c-601064ab2cac", title=None, description=None, gender=None, duration=None, movieRating=None, imgUrl=None, publicId=None,
                             imgUrlBackground=None, publicIdImgBackgound=None, statusMovie=None, base_64_img="seila_base_64")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.update_movie(movie_DTO)
        self.assertEqual(result.IsSuccess, False)

    def test_update_movie_delete_first_imgMain(self):
        movie_dto_database = MovieDTO(id=None, title=None, description=None, gender=None, duration=None, movieRating=None, imgUrl=None, publicId="publicId1",
                                      imgUrlBackground=None, publicIdImgBackgound="publicIdImgBackgound1", statusMovie=None, base_64_img=None)

        self.mock_movie_repository.get_by_id_only_publicId_PublicIdImgBackgound.return_value = ResponseWrapper.ok(
            movie_dto_database)

        self.mock_cloudinary_uti.delete_img.return_value = ResponseWrapper.fail(
            "error delete img main")

        movie_DTO = MovieDTO(id="961b70f2-232f-4a10-930c-601064ab2cac", title=None, description=None, gender=None, duration=None, movieRating=None, imgUrl=None, publicId=None,
                             imgUrlBackground=None, publicIdImgBackgound=None, statusMovie=None, base_64_img="seila_base_64")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.update_movie(movie_DTO)
        self.assertEqual(result.IsSuccess, False)

    def test_update_movie_delete_second_imgBackground(self):
        movie_dto_database = MovieDTO(id=None, title=None, description=None, gender=None, duration=None, movieRating=None, imgUrl=None, publicId="publicId1",
                                      imgUrlBackground=None, publicIdImgBackgound="publicIdImgBackgound1", statusMovie=None, base_64_img=None)

        self.mock_movie_repository.get_by_id_only_publicId_PublicIdImgBackgound.return_value = ResponseWrapper.ok(
            movie_dto_database)

        self.mock_cloudinary_uti.delete_img.side_effect = [
            ResponseWrapper.ok("deleted img main cloudinary"),
            ResponseWrapper.fail("error delete img background")
        ]

        self.mock_movie_repository.update_movie.return_value = ResponseWrapper.ok(
            "updated successfully")

        movie_DTO = MovieDTO(id="961b70f2-232f-4a10-930c-601064ab2cac", title=None, description=None, gender=None, duration=None, movieRating=None, imgUrl=None, publicId=None,
                             imgUrlBackground=None, publicIdImgBackgound=None, statusMovie=None, base_64_img="seila_base_64")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.update_movie(movie_DTO)
        self.assertEqual(result.IsSuccess, False)

    def test_update_movie_create_first_imgMain(self):
        movie_dto_database = MovieDTO(id=None, title=None, description=None, gender=None, duration=None, movieRating=None, imgUrl=None, publicId="publicId1",
                                      imgUrlBackground=None, publicIdImgBackgound="publicIdImgBackgound1", statusMovie=None, base_64_img=None)

        self.mock_movie_repository.get_by_id_only_publicId_PublicIdImgBackgound.return_value = ResponseWrapper.ok(
            movie_dto_database)

        self.mock_cloudinary_uti.delete_img.side_effect = [
            ResponseWrapper.ok("deleted img main cloudinary"),
            ResponseWrapper.ok("deleted img background cloudinary")
        ]

        self.mock_cloudinary_uti.create_img.return_value = ResponseWrapper.fail(
            "was not created, first imgMain")

        movie_DTO = MovieDTO(id="961b70f2-232f-4a10-930c-601064ab2cac", title=None, description=None, gender=None, duration=None, movieRating=None, imgUrl=None, publicId=None,
                             imgUrlBackground=None, publicIdImgBackgound=None, statusMovie=None, base_64_img="seila_base_64")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.update_movie(movie_DTO)
        self.assertEqual(result.IsSuccess, False)

    def test_update_movie_create_second_imgBackground(self):
        movie_dto_database = MovieDTO(id=None, title=None, description=None, gender=None, duration=None, movieRating=None, imgUrl=None, publicId="publicId1",
                                      imgUrlBackground=None, publicIdImgBackgound="publicIdImgBackgound1", statusMovie=None, base_64_img=None)

        self.mock_movie_repository.get_by_id_only_publicId_PublicIdImgBackgound.return_value = ResponseWrapper.ok(
            movie_dto_database)

        self.mock_cloudinary_uti.delete_img.side_effect = [
            ResponseWrapper.ok("deleted img main cloudinary"),
            ResponseWrapper.ok("deleted img background cloudinary")
        ]

        self.mock_cloudinary_uti.create_img.return_value = ResponseWrapper.fail(
            "was not created, first imgMain")

        self.mock_cloudinary_uti.create_img.side_effect = [
            ResponseWrapper.ok(CloudinaryCreate("public_id1", "image_url1")),
            ResponseWrapper.fail(
                "was not created, first imgBackground")
        ]

        movie_DTO = MovieDTO(id="961b70f2-232f-4a10-930c-601064ab2cac", title=None, description=None, gender=None, duration=None, movieRating=None, imgUrl=None, publicId=None,
                             imgUrlBackground=None, publicIdImgBackgound=None, statusMovie=None, base_64_img="seila_base_64")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.update_movie(movie_DTO)
        self.assertEqual(result.IsSuccess, False)

    def test_update_movie_error_when_updated_movie(self):
        movie_dto_database = MovieDTO(id=None, title=None, description=None, gender=None, duration=None, movieRating=None, imgUrl=None, publicId="publicId1",
                                      imgUrlBackground=None, publicIdImgBackgound="publicIdImgBackgound1", statusMovie=None, base_64_img=None)

        self.mock_movie_repository.get_by_id_only_publicId_PublicIdImgBackgound.return_value = ResponseWrapper.ok(
            movie_dto_database)

        self.mock_cloudinary_uti.delete_img.side_effect = [
            ResponseWrapper.ok("deleted img main cloudinary"),
            ResponseWrapper.ok("deleted img background cloudinary")
        ]

        self.mock_cloudinary_uti.create_img.side_effect = [
            ResponseWrapper.ok(CloudinaryCreate("public_id1", "image_url1")),
            ResponseWrapper.ok(CloudinaryCreate("public_id2", "image_url2"))
        ]

        self.mock_movie_repository.update_movie.return_value = ResponseWrapper.fail(
            "Failed to update movie")

        movie_DTO = MovieDTO(id="961b70f2-232f-4a10-930c-601064ab2cac", title=None, description=None, gender=None, duration=None, movieRating=None, imgUrl=None, publicId=None,
                             imgUrlBackground=None, publicIdImgBackgound=None, statusMovie=None, base_64_img="seila_base_64")

        movie_service = MovieService(self.mock_movie_repository, self.mock_movie_theater_service,
                                     self.mock_region_service, self.mock_cloudinary_uti)

        result = movie_service.update_movie(movie_DTO)
        self.assertEqual(result.IsSuccess, False)
