import time, logging
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app.utils import detect_objects, load_model

bp = Blueprint("main", __name__)

@bp.route("/detect", methods=["POST"])
@cross_origin()
def detect():
    start_time = time.time()
    logging.basicConfig(level=logging.DEBUG)
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    image_bytes = file.read()  # đọc toàn bộ bytes

    print("🖼 Received image of size:", len(image_bytes), "bytes")

    objects = detect_objects(image_bytes)

    print(f"[📤 Response time] {time.time() - start_time:.2f}s")
    return jsonify({"objects": objects})