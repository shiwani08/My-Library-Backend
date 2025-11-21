from flask import Blueprint
from app.books.controller import BookController

book_bp = Blueprint("book_bp", __name__)

book_bp.route("/add-book", methods=["POST"])(BookController.add_book)
book_bp.route("/get-books", methods=["GET"])(BookController.get_books)
book_bp.route("/get-book", methods=["GET"])(BookController.get_book_title)
book_bp.route("/update-book/<book_id>", methods=["PUT"])(BookController.update_book)
book_bp.route("/delete-book/<book_id>", methods=["DELETE"])(BookController.delete_book)

# from flask import Blueprint
# from app.books.controller import BookController
# from app.core.routes import BaseRoutes

# book_bp = Blueprint("book_bp", __name__)
# register_routes = BaseRoutes.register_standard_routes

# # Register all book routes
# register_routes(book_bp, [
#     ("/add-book", ["POST"], BookController.add_book),
#     ("/get-books", ["GET"], BookController.get_books),
#     ("/get-book", ["GET"], BookController.get_book_title),
#     ("/update-book/<book_id>", ["PUT"], BookController.update_book),
#     ("/delete-book/<book_id>", ["DELETE"], BookController.delete_book),
# ])