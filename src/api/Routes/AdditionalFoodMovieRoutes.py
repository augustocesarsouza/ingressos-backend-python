from flask import Blueprint, request, jsonify

from src.api.Adapters.RequestAdapter import request_adapter
from src.infradata.TokenVerify.TokenVerifies import token_verify
from src.infraioc.DependencyInjection import AdditionalFoodMovieControllerInjection

additional_food_movie_routes_bp = Blueprint(
    "additional_food_movie_routes", __name__)


@additional_food_movie_routes_bp.route('/v1/additionalfoodmovie/getallfood/<movieId>', methods=["GET"])
def get_all_food_movie(movieId: str):
    additional_food_movie_controller = AdditionalFoodMovieControllerInjection

    http_response = request_adapter(
        request, additional_food_movie_controller.additional_food_movie_controller_injection().get_all_food_movie)

    return jsonify(http_response.body), http_response.status_code


@additional_food_movie_routes_bp.route('/v1/additionalfoodmovie/create', methods=["POST"])
def create():
    additional_food_movie_controller = AdditionalFoodMovieControllerInjection

    http_response = request_adapter(
        request, additional_food_movie_controller.additional_food_movie_controller_injection().create)

    return jsonify(http_response.body), http_response.status_code
