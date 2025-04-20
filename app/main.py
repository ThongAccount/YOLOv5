from flask import Blueprint, request, jsonify
from app.utils import detect_objects

bp = Blueprint("main", __name__)

@bp.route("/detect", methods=["POST"])
def detect():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    image_bytes = file.read()  # đọc toàn bộ bytes

    objects = detect_objects(image_bytes)

    return jsonify({"objects": objects})