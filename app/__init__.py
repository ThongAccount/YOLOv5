from flask import Flask
from flask_cors import CORS  # <- thêm dòng này
from app import main

bp = main.bp

def create_app():
    app = Flask(__name__)
    CORS(app)  # <- bật CORS toàn cục
    app.register_blueprint(bp)
    return app
