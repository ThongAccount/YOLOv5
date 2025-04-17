from flask import Flask, request, jsonify
from flask import Flask
from flask_cors import CORS
from app.utils import detect_objects

app = Flask(__name__)
CORS(app)  # Cho phép tất cả domain truy cập API

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    results = detect_objects(file)
    return jsonify({'objects': results})
