from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_cors import CORS

mongo = PyMongo()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config["MONGO_URI"] = "mongodb+srv://shiwanisoni_db_user:PVjCLLnROFSJUAu1@library-cluster.80xdlxk.mongodb.net/my_library_db?retryWrites=true&w=majority"
    app.config["SECRET_KEY"] = "supersecretkey"

    mongo.init_app(app)
    bcrypt.init_app(app)

    return app
