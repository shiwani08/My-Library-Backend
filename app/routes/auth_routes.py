from flask import Blueprint
from app.controllers.auth_controller import AuthController

user_bp = Blueprint("user_bp", __name__)

user_bp.route("/signup", methods=["POST"])(AuthController.signup)
user_bp.route("/users", methods=["GET"])(AuthController.get_users)
