import jwt
from datetime import datetime, timedelta
from config import Config

def generate_token(data):
    payload = {
        "user_id": str(data["_id"]),
        "email": data["email"],
        "exp": datetime.utcnow() + timedelta(seconds=Config.TOKEN_EXPIRATION) 
    }

    print(data)

    return jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")