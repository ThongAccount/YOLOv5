from flask import Flask, request, jsonify
from flask_cors import CORS
from app.utils import detect_objects

app = Flask(__name__)
CORS(app)  # Cho phép mọi domain, hoặc chỉnh origin tùy bạn

@app.route("/detect", methods=["POST"])
def detect():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]
    result = detect_objects(image)
    return jsonify({"objects": result})
