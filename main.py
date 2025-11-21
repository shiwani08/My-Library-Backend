import os
from app.core.config import create_app, mongo
from app.auth.routes import user_bp
from app.books.routes import book_bp
from flask import jsonify

app = create_app()

@app.route("/test-db")
def test_db():
    try:
        mongo.db.command("ping")
        return jsonify({"status": "success", "message": "MongoDB connection OK"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Register blueprints
app.register_blueprint(user_bp)
app.register_blueprint(book_bp)

if __name__ == "__main__":
    app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port)
