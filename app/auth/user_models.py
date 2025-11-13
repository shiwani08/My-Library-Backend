import uuid
from datetime import datetime, timedelta, timezone
from app.config.config import mongo, bcrypt

class UserModel:
    @staticmethod
    def find_by_email(email):
        return mongo.db.users.find_one({"email": email})

    @staticmethod
    def find_by_username(username):
        return mongo.db.users.find_one({"username": username})

    @staticmethod
    def insert_user(user_data):
        return mongo.db.users.insert_one(user_data)

    @staticmethod
    def get_all_users():
        users = list(mongo.db.users.find({}, {"password": 0}))
        for user in users:
            user["_id"] = str(user["_id"])
        return users
    
    @staticmethod
    def update_password(email, new_password):
        hashed_pw = bcrypt.generate_password_hash(new_password).decode("utf-8")
        mongo.db.users.update_one(
            {"email": email},
            {"$set": {"password": hashed_pw, "updated_at": datetime.now(timezone.utc)}}
        )
        return True

    @staticmethod
    def create_reset_token(email):
        token = str(uuid.uuid4())
        expires_at = datetime.now(timezone.utc) + timedelta(minutes=15)
        mongo.db.password_resets.insert_one({
            "email": email,
            "token": token,
            "expires_at": expires_at
        })
        return token

    @staticmethod
    def verify_reset_token(token):
        reset_entry = mongo.db.password_resets.find_one({"token": token})
        if not reset_entry:
            return None
        
        if reset_entry["expires_at"] < datetime.utcnow():
            mongo.db.password_resets.delete_one({"token": token})
            return None
        return reset_entry["email"]
    