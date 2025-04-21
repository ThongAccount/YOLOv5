from flask import Flask
from flask_cors import CORS
from app.main import bp as main_blueprint
from app.utils import load_model

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(main_blueprint)
    
    # Load YOLO model at app startup
    load_model()

    return app
