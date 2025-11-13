from flask import Blueprint
from app.auth.auth_controller import AuthController

user_bp = Blueprint("user_bp", __name__)

user_bp.route("/signup", methods=["POST"])(AuthController.signup)
user_bp.route("/users", methods=["GET"])(AuthController.get_users)
user_bp.route("/login", methods=["POST"])(AuthController.login)
user_bp.route("/forgot-username", methods=["POST"])(AuthController.forgot_username)
user_bp.route("/forgot-password", methods=["POST"])(AuthController.forgot_password)
user_bp.route("/reset-password/<token>", methods=["PUT"])(AuthController.reset_password)
