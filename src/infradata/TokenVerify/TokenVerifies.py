from flask import jsonify, request
from functools import wraps
import jwt
import time
from src.infradata.Config.JwtConfigFile import jwt_config


def token_verify(function: callable) -> callable:

    @wraps(function)
    def decorated(*agr, **kwargs):
        raw_token = request.headers.get("Authorization")
        userID = request.headers.get("userID")

        if not raw_token or not userID:
            return jsonify({
                'error': 'Não Autorizado'
            }), 400

        if not raw_token:
            return jsonify({
                'error': 'Não Autorizado'
            }), 401

        try:
            token = raw_token.split()[1]
            token_information = jwt.decode(
                token, key=jwt_config["TOKEN_KEY"], algorithms="HS256")
            token_userID = token_information["userID"]
        except jwt.InvalidSignatureError:
            return jsonify({
                "error": "Token Invalido"
            }), 401
        except jwt.ExpiredSignatureError:
            return jsonify({
                "error": "Token Expirado"
            }), 401
        except KeyError as e:
            return jsonify({
                "error": "Token Invalido2"
            }), 401

        if userID != token_userID:
            return jsonify({
                'error': "user nao permitido"
            }), 400

        TOKEN_KEY = jwt_config["TOKEN_KEY"]
        REFRESH_TIME_MIN = jwt_config["REFRESH_TIME_MIN"]

        exp_time = token_information["exp"]

        time_exp = (exp_time - time.time()) / 60

        if time_exp <= 0:
            return jsonify({
                'error': "token expirado"
            }), 403

        return function(*agr, **kwargs)

    return decorated
