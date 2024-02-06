from flask import Flask
from src.api.Routes.UserRoutes import user_routes_bp
from src.api.Routes.AdditionalInfoRoutes import additional_info_routes_bp
from src.api.Routes.MovieRoutes import movie_routes_bp
from src.api.Routes.RegionRoutes import region_routes_bp
from src.api.Routes.TheatreRoutes import theatre_routes_bp
from src.api.Routes.CinemaRoutes import cinema_routes_bp
from src.api.Routes.CinemaMovieRoutes import cinema_movie_routes_bp
from src.api.Routes.MovieRegionTicketsPurchesedRoutes import movie_region_tickets_routes_bp
from src.api.Routes.FormOfPaymentRoutes import form_of_payment_routes_bp
from src.api.Routes.AdditionalFoodMovieRoutes import additional_food_movie_routes_bp

app = Flask(__name__)

app.register_blueprint(user_routes_bp)
app.register_blueprint(additional_info_routes_bp)
app.register_blueprint(movie_routes_bp)
app.register_blueprint(region_routes_bp)
app.register_blueprint(theatre_routes_bp)
app.register_blueprint(cinema_routes_bp)
app.register_blueprint(cinema_movie_routes_bp)
app.register_blueprint(movie_region_tickets_routes_bp)
app.register_blueprint(form_of_payment_routes_bp)
app.register_blueprint(additional_food_movie_routes_bp)
