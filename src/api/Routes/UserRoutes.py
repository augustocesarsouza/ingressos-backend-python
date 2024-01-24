from flask import Blueprint, request, jsonify

from src.api.Adapters.RequestAdapter import request_adapter
from src.infraioc.DependencyInjection import UserControllerInjection
from src.infradata.TokenVerify.TokenVerifies import token_verify

user_routes_bp = Blueprint("user_routes", __name__)


@user_routes_bp.route('/v1/user/create', methods=["POST"])
def register_user():
    user_controller = UserControllerInjection

    http_response = request_adapter(
        request, user_controller.user_menagement_controller_injection().create_async)

    return jsonify(http_response.body), http_response.status_code


@user_routes_bp.route('/v1/user/login/<cpfOrEmail>/<password>', methods=["GET"])
def login(cpfOrEmail: str, password: str):
    user_controller = UserControllerInjection

    http_response = request_adapter(
        request, user_controller.user_menagement_controller_injection().login_user)

    return jsonify(http_response.body), http_response.status_code


@user_routes_bp.route('/v1/user/verific/<code>/<guidId>', methods=["GET"])
@token_verify
def verfic(code: str, guidId: str):
    user_controller = UserControllerInjection

    http_response = request_adapter(
        request, user_controller.user_menagement_controller_injection().verfic_token)

    return jsonify(http_response.body), http_response.status_code


@user_routes_bp.route('/v1/user/confirm-token/<token>', methods=["GET"])
def get_confirm_token_user(token: str):
    user_controller = UserControllerInjection

    http_response = request_adapter(
        request, user_controller.user_menagement_controller_injection().get_confirm_token)

    return jsonify(http_response.body), http_response.status_code
