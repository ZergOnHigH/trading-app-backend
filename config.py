import os
from dotenv import load_dotenv
from extensions import mongodb, jwt
load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    