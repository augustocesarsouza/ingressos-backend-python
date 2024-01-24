from flask import Flask
from src.api.Routes.UserRoutes import user_routes_bp

app = Flask(__name__)

app.register_blueprint(user_routes_bp)
