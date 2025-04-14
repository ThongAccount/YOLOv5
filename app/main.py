from flask import request, jsonify
from app import bp
from app.utils import detect_objects  # Giả sử bạn có hàm detect_objects

@bp.route('/detect', methods=['POST'])
def detect():
    image = request.files.get('image')
    if image:
        result = detect_objects(image)  # Hàm xử lý ảnh
        return jsonify(result)  # Trả kết quả dưới dạng JSON
    return jsonify({"error": "No image provided"}), 400
