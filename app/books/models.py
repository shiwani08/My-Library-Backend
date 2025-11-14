from flask import request, jsonify
from app.config.config import mongo
from bson import ObjectId

class BookModel:
    STATUS_COLORS = {
        "currently-reading": "geekblue",
        "have-read": "green",
        "to-be-read": "gold"
    }
    
    @staticmethod
    def add_book(title, author, status):
        color = BookModel.STATUS_COLORS.get(status, "default")
        book_data = {"title": title, "author": author, "status": status, "color": color}
        result = mongo.db.books.insert_one(book_data)
        return str(book_data)

    @staticmethod
    def get_all_books():
        books = list(mongo.db.books.find())
        for book in books:
            book["_id"] = str(book["_id"])
        return books
    
    @staticmethod
    def get_book_title(title):
        book = mongo.db.books.find_one({"title": title})
        if book:
            book["_id"] = str(book["_id"])
        if "color" not in book:
            book["color"] = BookModel.STATUS_COLORS.get(book["status"], "default")
        return book
    
    @staticmethod
    def update_book(book_id, title=None, author=None, status=None):
        book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
        if not book:
            return None
        
        update_data = {}
        if title:
            update_data["title"] = title
        if author:
            update_data["author"] = author
        if status:
            update_data["status"] = status
            update_data["color"] = BookModel.STATUS_COLORS.get(status, "default")

        mongo.db.books.update_one({"_id": ObjectId(book_id)}, {"$set": update_data})
        
        updated_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
        updated_book["_id"] = str(updated_book["_id"])
        return updated_book

    @staticmethod
    def delete_book(book_id):
        result = mongo.db.books.delete_one({"_id": ObjectId(book_id)})
        return result.deleted_count > 0
