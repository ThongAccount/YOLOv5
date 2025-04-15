from flask import request, jsonify
from app import bp
from app.utils import detect_objects  # hoặc tên hàm bạn đặt

@bp.route("/detect", methods=["POST"])
def detect():
    file = request.files["image"]
    result = detect_objects(file)  # file là ảnh từ form
    return jsonify({"objects": result})
