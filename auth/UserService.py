from auth.UserModel import UserModel
from extensions import mongodb
from utils.generate_token import generate_token
from bson import ObjectId

class UserService:

    @staticmethod
    def get_repo():
        return mongodb.get_collection("users")

    @staticmethod
    def create_user(data):
        if UserService.email_exists(data["email"]):
            raise Exception("Email już zarejestrowany")

        model = UserModel().load(data)
        print(model)

        UserService.get_repo().insert_one(model)

    @staticmethod
    def login_user(data):
        user = UserService.email_exists(data["email"])
        if not user:
            raise Exception("Nie znaleziono użytkownika")
        if not UserModel.check_password(user["password"],data["password"]):
            raise Exception("Nieprawidłowe hasło")

        token = generate_token(user)
        return token

    @staticmethod 
    def change_password(data, id):

        if not data["old_password"] or not data["new_password"]:
            raise Exception("Hasło nie może być puste")
        
        UserService.get_repo().update_one(
            {"_id": ObjectId(id)},
            {"$set": {"password": UserModel.hash_password(data["new_password"])}}
        )
        return True



        


    @staticmethod
    def email_exists(email):
        user = UserService.get_repo().find_one({"email": email})
        return user