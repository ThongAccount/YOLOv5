from flask import Flask
from app import bp  # Import Blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

app.register_blueprint(bp)  # Đăng ký Blueprint

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
