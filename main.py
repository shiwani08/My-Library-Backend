from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from bson import ObjectId

# --- Configuration ---
app = Flask(__name__)
CORS(app)  # allow frontend connections (e.g., from Next.js)

app.config["MONGO_URI"] = "mongodb+srv://shiwanisoni_db_user:PVjCLLnROFSJUAu1@library-cluster.80xdlxk.mongodb.net/my_library_db?retryWrites=true&w=majority"
app.config["SECRET_KEY"] = "supersecretkey"

# --- Initialize extensions ---
mongo = PyMongo(app)
bcrypt = Bcrypt(app)

# --- Test DB connection route ---
@app.route("/test-db")
def test_db():
    try:
        mongo.db.command("ping")
        return jsonify({"status": "success", "message": "MongoDB connection OK"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# --- Signup Route ---
@app.route("/signup", methods=["POST"])
def signup():
    try:
        data = request.get_json()
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not username or not email or not password:
            return jsonify({"error": "All fields are required"}), 400

        existing_user = mongo.db.users.find_one({"email": email})
        if existing_user:
            return jsonify({"error": "User already exists"}), 400

        hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
        user = {
            "username": username,
            "email": email,
            "password": hashed_pw,
        }

        result = mongo.db.users.insert_one(user)
        return jsonify({
            "message": "User created successfully",
            "user_id": str(result.inserted_id)
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# --- Just for testing: get all users ---
@app.route("/users", methods=["GET"])
def get_users():
    try:
        users = list(mongo.db.users.find({}, {"password": 0}))  # hide password
        for user in users:
            user["_id"] = str(user["_id"])
        return jsonify(users)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
