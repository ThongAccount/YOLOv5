from flask import Blueprint, request, jsonify
from app.utils import detect_objects
import os

bp = Blueprint("main", __name__)

@bp.route("/detect", methods=["POST"])
def detect():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    path = os.path.join("temp.jpg")
    file.save(path)

    labels = detect_objects(path)
    os.remove(path)
    return jsonify({"objects": labels})
