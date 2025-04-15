from flask import Blueprint

bp = Blueprint("main", __name__)

from app import main  # Đảm bảo import route ở đây
