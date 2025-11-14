from flask import Blueprint
from app.books.controller import BookController

book_bp = Blueprint("book_bp", __name__)

book_bp.route("/add-book", methods=["POST"])(BookController.add_book)
book_bp.route("/get-books", methods=["GET"])(BookController.get_books)
book_bp.route("/get-book", methods=["GET"])(BookController.get_book_title)
book_bp.route("/update-book/<book_id>", methods=["PUT"])(BookController.update_book)
book_bp.route("/delete-book/<book_id>", methods=["DELETE"])(BookController.delete_book)