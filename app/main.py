from flask import Blueprint, request, jsonify
from app.utils import detect_objects
import cv2
import numpy as np

bp = Blueprint("main", __name__)

@bp.route("/detect", methods=["POST"])
def detect():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    npimg = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    objects = detect_objects(image)
    return jsonify({"objects": objects})
