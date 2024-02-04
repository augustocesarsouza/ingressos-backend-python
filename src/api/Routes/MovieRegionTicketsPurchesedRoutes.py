from flask import Blueprint, request, jsonify

from src.api.Adapters.RequestAdapter import request_adapter
from src.infradata.TokenVerify.TokenVerifies import token_verify
from src.infraioc.DependencyInjection import MovieRegionTicketsPurchesedControllerInjection

movie_region_tickets_routes_bp = Blueprint(
    "movie_region_tickets_routes", __name__)


@movie_region_tickets_routes_bp.route('/v1/movieregiontickets/getbymovieidandcinemaid/<movieId>/<cinemaId>', methods=["GET"])
def get_by_movie_id_and_cinema_id(movieId: str, cinemaId: str):
    cinema_movie_controller = MovieRegionTicketsPurchesedControllerInjection

    http_response = request_adapter(
        request, cinema_movie_controller.movie_region_controller_injection().get_by_movie_id_and_cinema_id)

    return jsonify(http_response.body), http_response.status_code


@movie_region_tickets_routes_bp.route('/v1/movieregiontickets/create', methods=["POST"])
def create():
    cinema_movie_controller = MovieRegionTicketsPurchesedControllerInjection

    http_response = request_adapter(
        request, cinema_movie_controller.movie_region_controller_injection().create)

    return jsonify(http_response.body), http_response.status_code


@movie_region_tickets_routes_bp.route('/v1/movieregiontickets/update', methods=["PUT"])
def update():
    cinema_movie_controller = MovieRegionTicketsPurchesedControllerInjection

    http_response = request_adapter(
        request, cinema_movie_controller.movie_region_controller_injection().update)

    return jsonify(http_response.body), http_response.status_code
