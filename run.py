from src.api.Server.Server import app
from src.application.Services.MovieService import MovieService
from src.application.Services.MovieTheaterService import MovieTheaterService
from src.infradata.Repositories.MovieRepository import MovieRepository
from src.infradata.Repositories.MovieTheaterRepository import MovieTheaterRepository

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
