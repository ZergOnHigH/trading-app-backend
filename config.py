import os
from dotenv import load_dotenv
load_dotenv()

class Config: 
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DB = os.getenv("MONGO_DB")
    TOKEN_EXPIRATION = int(os.getenv("TOKEN_EXPIRATION"))
    SECRET_KEY = os.getenv("SECRET_KEY")
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")
    CLIENT_URL= os.getenv("CLIENT_URL")
    # DOCX_TEMPLATE = os.getenv("DOCX_TEMPLATE")