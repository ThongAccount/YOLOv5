from flask import Blueprint, request, jsonify
import time
from app.utils import detect_objects

main = Blueprint("main", __name__)

@main.route("/detect", methods=["POST"])
def detect():
    start_time = time.time()

    if "image" not in request.files:
        return jsonify({"error": "Missing image file"}), 400

    image_file = request.files["image"]
    image_bytes = image_file.read()

    print(f"🖼 Received image of size: {len(image_bytes)} bytes")

    try:
        objects = detect_objects(image_bytes)
    except Exception as e:
        print(f"[❌ Error] {e}")
        return jsonify({"error": "Detection failed", "detail": str(e)}), 500

    response_time = time.time() - start_time
    print(f"[📤 Response time] {response_time:.2f}s")

    return jsonify({"objects": objects, "time": round(response_time, 2)})
