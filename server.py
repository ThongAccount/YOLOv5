from flask import Flask
from app import bp
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.register_blueprint(bp)  # ← Đăng ký blueprint

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
