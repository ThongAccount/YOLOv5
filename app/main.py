from flask import Blueprint, request, jsonify
from app.utils import detect_objects
import os

bp = Blueprint("main", __name__)

@bp.route("/detect", methods=["POST"])
def detect():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['image']
    image_bytes = image_file.read()
    results = detect_objects(image_bytes)  # <-- your detection function

    return jsonify({'results': results})