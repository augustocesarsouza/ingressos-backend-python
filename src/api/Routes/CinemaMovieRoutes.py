from flask import Blueprint, request, jsonify

from src.api.Adapters.RequestAdapter import request_adapter
from src.infradata.TokenVerify.TokenVerifies import token_verify
from src.infraioc.DependencyInjection import CinemaMovieControllerInjection

cinema_movie_routes_bp = Blueprint("cinema_movie_routes", __name__)


@cinema_movie_routes_bp.route('/v1/cinemaMovie/getAll/<region>/<movieId>', methods=["GET"])
def get_by_region_cinema_id_and_movie_id(region: str, movieId: str):
    cinema_movie_controller = CinemaMovieControllerInjection

    http_response = request_adapter(
        request, cinema_movie_controller.cinema_movie_controller_injection().get_by_region_cinema_id_and_movie_id)

    return jsonify(http_response.body), http_response.status_code


@cinema_movie_routes_bp.route('/v1/cinemaMovie/create', methods=["POST"])
def create():
    cinema_movie_controller = CinemaMovieControllerInjection

    http_response = request_adapter(
        request, cinema_movie_controller.cinema_movie_controller_injection().create)

    return jsonify(http_response.body), http_response.status_code
