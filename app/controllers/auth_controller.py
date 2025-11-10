from flask import jsonify, request
from app.config.config import bcrypt
from app.models.user_models import UserModel

class AuthController:
    @staticmethod
    def signup():
        try:
            data = request.get_json()
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            if not username or not email or not password:
                return jsonify({"error": "All fields are required"}), 400

            if UserModel.find_by_email(email):
                return jsonify({"error": "User already exists"}), 400

            hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
            user = {"username": username, "email": email, "password": hashed_pw}

            result = UserModel.insert_user(user)
            return jsonify({
                "message": "User created successfully",
                "user_id": str(result.inserted_id)
            }), 201

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_users():
        try:
            users = UserModel.get_all_users()
            return jsonify(users), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
