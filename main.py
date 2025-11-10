from app.config.config import create_app, mongo
from app.routes.auth_routes import user_bp
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

if __name__ == "__main__":
    app.run(debug=True)
