from flask import Flask
from src.api.Routes.UserRoutes import user_routes_bp
from src.api.Routes.AdditionalInfoRoutes import additional_info_routes_bp
from src.api.Routes.MovieRoutes import movie_routes_bp
from src.api.Routes.RegionRoutes import region_routes_bp
from src.api.Routes.TheatreRoutes import theatre_routes_bp

app = Flask(__name__)

app.register_blueprint(user_routes_bp)
app.register_blueprint(additional_info_routes_bp)
app.register_blueprint(movie_routes_bp)
app.register_blueprint(region_routes_bp)
app.register_blueprint(theatre_routes_bp)
