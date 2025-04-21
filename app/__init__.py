from flask import Flask
from app.main import main as main_blueprint
from app.utils import load_model

def create_app():
    app = Flask(__name__)
    
    # Load model only once at startup
    load_model()

    app.register_blueprint(main_blueprint)

    return app
