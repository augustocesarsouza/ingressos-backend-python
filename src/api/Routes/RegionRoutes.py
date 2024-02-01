from flask import Blueprint, request, jsonify

from src.api.Adapters.RequestAdapter import request_adapter
from src.infradata.TokenVerify.TokenVerifies import token_verify
from src.infraioc.DependencyInjection import RegionControllerInjection

region_routes_bp = Blueprint("region_routes", __name__)


@region_routes_bp.route('/v1/region/by-name-city/<state>', methods=["GET"])
def get_id_by_name_state(state: str):
    movie_controller = RegionControllerInjection

    http_response = request_adapter(
        request, movie_controller.region_controller_injection().get_all_movie_by_region_id)

    return jsonify(http_response.body), http_response.status_code
