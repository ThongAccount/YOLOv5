from flask import request, jsonify
from app import bp
from app.utils import detect_objects
import os
from werkzeug.utils import secure_filename

bp = Blueprint("bp", __name__)

@bp.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    filename = secure_filename(image.filename)
    image_path = os.path.join('/tmp', filename)
    image.save(image_path)

    objects = detect_objects(image_path)
    return jsonify({'objects': objects})
