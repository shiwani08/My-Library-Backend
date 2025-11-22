# not using the core modules
# from flask import request, jsonify
# from app.core.config import mongo
# from bson import ObjectId

# class BookModel:
#     STATUS_COLORS = {
#         "currently-reading": "geekblue",
#         "have-read": "green",
#         "to-be-read": "gold"
#     }
    
#     @staticmethod
#     def add_book(title, author, status, description, ratings=None):
#         color = BookModel.STATUS_COLORS.get(status, "default")
#         book_data = {"title": title, "author": author, "status": status, "color": color, "description": description, "ratings": ratings}
#         result = mongo.db.books.insert_one(book_data)
#         return str(result.inserted_id)

#     @staticmethod
#     def get_all_books():
#         books = list(mongo.db.books.find())
#         for book in books:
#             book["_id"] = str(book["_id"])
#         return books
    
#     @staticmethod
#     def get_book_title(title):
#         book = mongo.db.books.find_one({"title": title})
#         if book:
#             book["_id"] = str(book["_id"])
#         if "color" not in book:
#             book["color"] = BookModel.STATUS_COLORS.get(book["status"], "default")
#         return book
    
#     @staticmethod
#     def update_book(book_id, title=None, author=None, status=None, description=None, ratings=None):
#         book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
#         if not book:
#             return None
        
#         update_data = {}
#         if title:
#             update_data["title"] = title
#         if author:
#             update_data["author"] = author
#         if status:
#             update_data["status"] = status
#             update_data["color"] = BookModel.STATUS_COLORS.get(status, "default")
#         if description:
#             update_data["description"] = description
#         if ratings is not None:
#             update_data["ratings"] = ratings

#         mongo.db.books.update_one({"_id": ObjectId(book_id)}, {"$set": update_data})
        
#         updated_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
#         updated_book["_id"] = str(updated_book["_id"])
#         return updated_book

#     @staticmethod
#     def delete_book(book_id):
#         result = mongo.db.books.delete_one({"_id": ObjectId(book_id)})
#         return result.deleted_count > 0

# using the core modules
from app.core.models import BaseModel
class BookModel(BaseModel):
    collection_name = "books"
    
    STATUS_COLORS = {
        "currently-reading": "geekblue",
        "have-read": "green",
        "to-be-read": "gold"
    }
    
    @classmethod
    def before_insert(cls, data):
        
        # Automatically add color based on status
        if "status" in data and "color" not in data:
            data["color"] = cls.STATUS_COLORS.get(data["status"], "default")
        return data
    
    @classmethod
    def before_update(cls, current_document, update_data):
       
        # Update color if status is being changed
        if "status" in update_data:
            update_data["color"] = cls.STATUS_COLORS.get(update_data["status"], "default")
        return update_data
    
    @staticmethod
    def add_book(title, author, status, description, ratings=None):
        
        return BookModel.add(
            title=title,
            author=author,
            status=status,
            description=description,
            ratings=ratings
        )
    
    @staticmethod
    def get_all_books():
        
        return BookModel.get_all()
    
    @staticmethod
    def get_book_title(title):
        
        book = BookModel.get_by_field("title", title)
        
        # Ensure color is present (for backward compatibility)
        if book and "color" not in book:
            book["color"] = BookModel.STATUS_COLORS.get(book.get("status"), "default")
        
        return book
    
    @staticmethod
    def update_book(book_id, title=None, author=None, status=None, description=None, ratings=None):
        
        return BookModel.update(
            book_id,
            title=title,
            author=author,
            status=status,
            description=description,
            ratings=ratings
        )
    
    @staticmethod
    def delete_book(book_id):
       
        return BookModel.delete(book_id)
    
    # Additional custom methods
    @classmethod
    def get_books_by_status(cls, status):
        
        return cls.get_many_by_field("status", status)
    
    @classmethod
    def get_books_by_author(cls, author):
        
        return cls.get_many_by_field("author", author)
    
    @classmethod
    def search_books(cls, search_term):
        
        from app.core.config import mongo
        collection = cls.get_collection()
        
        # Case-insensitive search
        regex_pattern = {"$regex": search_term, "$options": "i"}
        query = {
            "$or": [
                {"title": regex_pattern},
                {"author": regex_pattern}
            ]
        }
        
        documents = list(collection.find(query))
        return cls.serialize_list(documents)