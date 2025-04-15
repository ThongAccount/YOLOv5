from flask import Blueprint
from .main import detect

bp = Blueprint("api", __name__)

# Đăng ký route detect
bp.add_url_rule("/detect", "detect", detect, methods=["POST"])
