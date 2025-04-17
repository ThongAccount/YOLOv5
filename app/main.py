<<<<<<< HEAD
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
=======
from flask import request, jsonify
from app import bp
from app.utils import detect_objects  # hoặc tên hàm bạn đặt

@bp.route("/detect", methods=["POST"])
def detect():
    file = request.files["image"]
    result = detect_objects(file)  # file là ảnh từ form
    return jsonify({"objects": result})
>>>>>>> parent of b2839bf (l)
