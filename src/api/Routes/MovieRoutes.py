from flask import Blueprint, request, jsonify

from src.api.Adapters.RequestAdapter import request_adapter
from src.infradata.TokenVerify.TokenVerifies import token_verify
from src.infraioc.DependencyInjection import MovieControllerInjection

movie_routes_bp = Blueprint("movie_routes", __name__)


@movie_routes_bp.route('/v1/movie/create', methods=["POST"])
def create():
    movie_controller = MovieControllerInjection

    http_response = request_adapter(
        request, movie_controller.movie_controller_injection().create)

    return jsonify(http_response.body), http_response.status_code


@token_verify
@movie_routes_bp.route('/v1/movie/get-all-region/<region>', methods=["GET"])
def get_all_movie_by_region_id(region: str):
    movie_controller = MovieControllerInjection

    http_response = request_adapter(
        request, movie_controller.movie_controller_injection().get_all_movie_by_region_id)

    return jsonify(http_response.body), http_response.status_code


@token_verify
@movie_routes_bp.route('/v1/movie/info/<idGuid>', methods=["GET"])
def get_info_movies_by_id(idGuid: str):
    movie_controller = MovieControllerInjection

    http_response = request_adapter(
        request, movie_controller.movie_controller_injection().get_info_movies_by_id)

    return jsonify(http_response.body), http_response.status_code


@token_verify
@movie_routes_bp.route('/v1/movie/get-status-movie/<statusMovie>', methods=["GET"])
def get_status_movie(statusMovie: str):
    movie_controller = MovieControllerInjection

    http_response = request_adapter(
        request, movie_controller.movie_controller_injection().get_status_movie)

    return jsonify(http_response.body), http_response.status_code


@token_verify
@movie_routes_bp.route('/v1/movie/delete/<idMovie>', methods=["DELETE"])
def delete(idMovie: str):
    movie_controller = MovieControllerInjection

    http_response = request_adapter(
        request, movie_controller.movie_controller_injection().delete_movie)

    return jsonify(http_response.body), http_response.status_code


@token_verify
@movie_routes_bp.route('/v1/movie/update', methods=["PUT"])
def update():
    movie_controller = MovieControllerInjection

    http_response = request_adapter(
        request, movie_controller.movie_controller_injection().update_movie)

    return jsonify(http_response.body), http_response.status_code
