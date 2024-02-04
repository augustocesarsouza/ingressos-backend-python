from src.api.Server.Server import app
from src.application.Services.MovieRegionTicketsPurchesedService import MovieRegionTicketsPurchesedService
from src.infradata.Repositories.MovieRegionTicketsPurchesedRepository import MovieRegionTicketsPurchesedRepository

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
