import os
from dotenv import load_dotenv
load_dotenv()

jwt_config = {
    "TOKEN_KEY": os.getenv("TOKEN_KEY"),
    "EXP_TIME_MIN": int(os.getenv("EXP_TIME_MIN")),
    "REFRESH_TIME_MIN": int(os.getenv("REFRESH_TIME_MIN")),
    "JWT_KEY": os.getenv("JWT_KEY"),
    "API-KEY-BREVO": os.getenv("API-KEY-BREVO"),
}
