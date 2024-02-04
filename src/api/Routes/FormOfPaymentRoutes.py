from flask import Blueprint, request, jsonify

from src.api.Adapters.RequestAdapter import request_adapter
from src.infradata.TokenVerify.TokenVerifies import token_verify
from src.infraioc.DependencyInjection import FormOfPaymentControllerInjection

form_of_payment_routes_bp = Blueprint("form_of_payment_routes", __name__)


@form_of_payment_routes_bp.route('/v1/formofpayment/get-form/<movieid>', methods=["GET"])
def get_movie_id_info(movieid: str):
    form_of_payment_controller = FormOfPaymentControllerInjection

    http_response = request_adapter(
        request, form_of_payment_controller.form_of_payment_controller_injection().get_movie_Id_info)

    return jsonify(http_response.body), http_response.status_code


@form_of_payment_routes_bp.route('/v1/formofpayment/create', methods=["POST"])
def create():
    form_of_payment_controller = FormOfPaymentControllerInjection

    http_response = request_adapter(
        request, form_of_payment_controller.form_of_payment_controller_injection().create)

    return jsonify(http_response.body), http_response.status_code
