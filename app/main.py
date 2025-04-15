from flask import Blueprint, request, jsonify
import os
from werkzeug.utils import secure_filename
from app.utils import detect_objects

bp = Blueprint("app", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@bp.route("/detect", methods=["POST"])
def detect():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    # Gọi model nhận diện
    try:
        objects = detect_objects(file_path)
        return jsonify({"objects": objects})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
