from flask import Blueprint, request, jsonify

from src.api.Adapters.RequestAdapter import request_adapter
from src.infradata.TokenVerify.TokenVerifies import token_verify
from src.infraioc.DependencyInjection import AdditionalInfoUserInjection

additional_info_routes_bp = Blueprint("additional_info_routes", __name__)


@additional_info_routes_bp.route("/v1/info-user/<idGuid>", methods=["GET"])
def get_info_user(idGuid: str):
    user_controller = AdditionalInfoUserInjection

    http_response = request_adapter(
        request, user_controller.user_additional_info_user_controller_injection().get_info_user)

    return jsonify(http_response.body), http_response.status_code


@additional_info_routes_bp.route("/v1/additional/update-info-user/<password>", methods=["PUT"])
def update_async(password: str):
    user_controller = AdditionalInfoUserInjection

    http_response = request_adapter(
        request, user_controller.user_additional_info_user_controller_injection().update_async)

    return jsonify(http_response.body), http_response.status_code
