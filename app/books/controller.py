# not using the core modules
# from flask import request, jsonify
# from app.books.models import BookModel

# class BookController:
#     @staticmethod
#     def add_book():
#         try:
#             data = request.get_json()
#             title = data.get("title")
#             author = data.get("author")
#             status = data.get("status")
#             description = data.get("description")
#             ratings = data.get("ratings")

#             if not title or not author or not status:
#                 return jsonify({"error": "Title, author, and status are required"}), 400

#             book_id = BookModel.add_book(title, author, status, description, ratings)
#             return jsonify({"message": "Book added successfully!!!!", "book_id!!": book_id, "status": status}), 201

#         except Exception as e:
#             return jsonify({"error": str(e)}), 500

#     @staticmethod
#     def get_books():
#         try:
#             books = BookModel.get_all_books()
#             return jsonify(books), 200
#         except Exception as e:
#             return jsonify({"error": str(e)}), 500

#     @staticmethod
#     def get_book_title():
#         try:
#             title = request.args.get("title")
#             if not title:
#                 return jsonify({"error": "Title parameter is required"}), 400

#             book = BookModel.get_book_title(title)
#             if not book:
#                 return jsonify({"error": "Book not found"}), 404

#             return jsonify(book), 200

#         except Exception as e:
#             return jsonify({"error": str(e)}), 500
        
#     @staticmethod
#     def update_book(book_id):
#         try:
#             data = request.get_json()
#             title = data.get("title")
#             author = data.get("author")
#             status = data.get("status")
#             description = data.get("description")
#             ratings = data.get("ratings")

#             updated_book = BookModel.update_book(book_id, title, author, status, description, ratings)
#             if not updated_book:
#                 return jsonify({"error": "Book not found"}), 404

#             return jsonify({
#                 "message": "Book updated successfully!",
#                 "book": updated_book
#             }), 200

#         except Exception as e:
#             return jsonify({"error": str(e)}), 500

#     @staticmethod
#     def delete_book(book_id):
#         try:
#             deleted = BookModel.delete_book(book_id)
#             if not deleted:
#                 return jsonify({"error": "Book not found"}), 404


#             return jsonify({"message": "Book deleted successfully!"}), 200

#         except Exception as e:
#             return jsonify({"error": str(e)}), 500

# using the core modules
from flask import request, jsonify
from app.books.models import BookModel
from app.core.controllers import BaseController

class BookController(BaseController):
    model_class = BookModel
    resource_name = "book"
    
    # make generic functions pass self
    @classmethod
    def get_required_fields(cls):
        return ["title", "author", "status"]
    
    @classmethod
    def get_search_field(cls):
        return "title"
    
    # Use inherited methods by aliasing them to match your naming convention
    @staticmethod
    def add_book():
        return BookController.add()
    
    @staticmethod
    def get_books():
        return BookController.get_all()
    
    @staticmethod
    def get_book_title():
        return BookController.get_by_query()
    
    @staticmethod
    def update_book(book_id):
        return BookController.update(book_id)
    
    @staticmethod
    def delete_book(book_id):
        return BookController.delete(book_id)
    
    # Add custom methods specific to books
    @staticmethod
    def search_by_author():
        
        try:
            author = request.args.get("author")
            if not author:
                return jsonify({"error": "Author parameter is required"}), 400
            
            books = BookModel.get_by_field("author", author)
            if not books:
                return jsonify({"error": "No books found for this author"}), 404
            
            return jsonify(books), 200
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500