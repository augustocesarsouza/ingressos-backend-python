from flask import Blueprint, request, jsonify

from src.api.Adapters.RequestAdapter import request_adapter
from src.infradata.TokenVerify.TokenVerifies import token_verify
from src.infraioc.DependencyInjection import TheatreControllerInjection

theatre_routes_bp = Blueprint("theatre_routes", __name__)


@theatre_routes_bp.route('/v1/theatre/get-all-region/<state>', methods=["GET"])
def get_all_theatre_by_state_name(state: str):
    theatre_controller = TheatreControllerInjection

    http_response = request_adapter(
        request, theatre_controller.theatre_controller_injection().get_all_theatre_by_state_name)

    return jsonify(http_response.body), http_response.status_code


@theatre_routes_bp.route('/v1/theatre/create', methods=["POST"])
def get_id_by_name_state():
    theatre_controller = TheatreControllerInjection

    http_response = request_adapter(
        request, theatre_controller.theatre_controller_injection().create)

    return jsonify(http_response.body), http_response.status_code


@theatre_routes_bp.route('/v1/theatre/delete/<idTheatre>', methods=["DELETE"])
def delete(idTheatre: str):
    theatre_controller = TheatreControllerInjection

    http_response = request_adapter(
        request, theatre_controller.theatre_controller_injection().delete)

    return jsonify(http_response.body), http_response.status_code


@theatre_routes_bp.route('/v1/theatre/update', methods=["PUT"])
def update():
    theatre_controller = TheatreControllerInjection

    http_response = request_adapter(
        request, theatre_controller.theatre_controller_injection().update)

    return jsonify(http_response.body), http_response.status_code
