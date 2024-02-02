from flask import Blueprint, request, jsonify

from src.api.Adapters.RequestAdapter import request_adapter
from src.infradata.TokenVerify.TokenVerifies import token_verify
from src.infraioc.DependencyInjection import CinemaControllerInjection

cinema_routes_bp = Blueprint("cinema_routes", __name__)


@cinema_routes_bp.route('/v1/cinema/create', methods=["POST"])
def create():
    cinema_controller = CinemaControllerInjection

    http_response = request_adapter(
        request, cinema_controller.cinema_controller_injection().create)

    return jsonify(http_response.body), http_response.status_code
