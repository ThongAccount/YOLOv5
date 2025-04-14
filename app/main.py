from flask import request, jsonify
from app import bp
from app.utils import detect_objects  # Giả sử bạn có hàm detect_objects

@bp.route("/detect", methods=["POST"])
def detect():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]
    result = detect_objects(image)
    return jsonify(result)
