from flask import Blueprint

bp = Blueprint("main", __name__)

from app import main  # ← PHẢI CÓ DÒNG NÀY để import routes từ main.py
