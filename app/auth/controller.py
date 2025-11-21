from flask import jsonify, request
from app.core.config import bcrypt
from app.auth.models import UserModel

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
                "user_id": str(result.inserted_id),
                "message": "User created successfully",
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
        
    @staticmethod
    def login():
        try: 
            data = request.get_json()  
            email = data.get("email")
            username = data.get("username")
            password = data.get("password")

            user = UserModel.find_by_email(email) or UserModel.find_by_username(username)
            if not user:
                return jsonify({"error": "User not found"}), 404

            if not bcrypt.check_password_hash(user["password"], password):
                return jsonify({"error": "Invalid password"}), 401

            return jsonify({
                "message": "Login successful",
                "user": {
                    "id": str(user["_id"]),
                    "username": user["username"],
                    "email": user["email"]
                }
            }), 200
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def forgot_username():
        try:
            data = request.get_json()
            email = data.get("email")

            if not email:
                return jsonify({"error": "Email is required"}), 400

            user = UserModel.find_by_email(email)
            if not user:
                return jsonify({"error": "User not found"}), 404

            # In real production, send this via email
            return jsonify({"message": "Username retrieved successfully", "username": user["username"]}), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @staticmethod
    def forgot_password():
        try:
            data = request.get_json()
            email = data.get("email")

            if not email:
                return jsonify({"error": "Email is required"}), 400

            user = UserModel.find_by_email(email)
            if not user:
                return jsonify({"error": "User not found"}), 404

            token = UserModel.create_reset_token(email)
            return jsonify({
                "message": "Password reset token generated. (Use this in reset-password API)",
                "reset_token": token
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @staticmethod
    def reset_password(token):
        try:
            data = request.get_json()
            new_password = data.get("new_password")

            if not new_password:
                return jsonify({"error": "New password is required"}), 400

            email = UserModel.verify_reset_token(token)
            if not email:
                return jsonify({"error": "Invalid or expired token"}), 400

            UserModel.update_password(email, new_password)
            return jsonify({"message": "Password updated successfully"}), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500