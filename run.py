from src.api.Server.Server import app
from src.application.Services.UserConfirmationService import UserConfirmationService
from src.infradata.Repositories.UserRepository import UserRepository
from src.infradata.UtilityExternal.SendEmailBrevo import SendEmailBrevo

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from src.infradata.UtilityExternal.CacheRedisUti import CacheRedisUti
cache_redis = CacheRedisUti()
# cache_redis.set_string_async_wrapper_expiry("nome", "augusto", 1)
# aqui = cache_redis.get_string_async_wrapper("nome")
# print(aqui)

# send_brevo = SendEmailBrevo()
# user = {"name": "augusto", "email": "augustocesarsantana53@gmail.com"}
# result = send_brevo.send_code(user, 123456)
# if result.IsSuccess:
#     print("true")

# user_repository = UserRepository()
# userConfirmationService = UserConfirmationService(user_repository, cache_redis)
# userConfirmationService.get_confirm_token(
#     "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDYwNDE2NTUsImlkIjoiYzFkNDY5OWQtZDIzZi00MTA3LTg0ZjgtMGI3NGEyN2QwMTk5In0.tPFkktWqhoVETmg-U1xrfHOTSLKMECAO89OsnVslypw")
