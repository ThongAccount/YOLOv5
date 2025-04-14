from flask import Blueprint

bp = Blueprint('main', __name__)

from app import main  # Import các routes của bạn
