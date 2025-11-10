from flask import request, jsonify
from app.config.config import mongo
from bson import ObjectId

class BookModel:
    @staticmethod
    def add_book(title, author):
        book_data = {"title": title, "author": author}
        result = mongo.db.books.insert_one(book_data)
        return str(result.inserted_id)

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
        return book


