from bson import ObjectId
from app.config.config import mongo

class UserModel:
    @staticmethod
    def find_by_email(email):
        return mongo.db.users.find_one({"email": email})

    @staticmethod
    def insert_user(user_data):
        return mongo.db.users.insert_one(user_data)

    @staticmethod
    def get_all_users():
        users = list(mongo.db.users.find({}, {"password": 0}))
        for user in users:
            user["_id"] = str(user["_id"])
        return users
