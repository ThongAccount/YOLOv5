from flask import Blueprint
from .main import detect  # hoặc import các route

bp = Blueprint("api", __name__)

# Đăng ký route
bp.add_url_rule("/detect", "detect", detect, methods=["POST"])
