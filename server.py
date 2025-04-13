from flask import Flask
from flask_cors import CORS
from app import bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(bp)

@app.route('/')
def index():
    return "YOLOv5n Object Detection API is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
