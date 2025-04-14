from ultralytics import YOLO
from PIL import Image
import numpy as np

# Dùng mô hình nhẹ nhất và tương thích tốt
model = YOLO("yolov5nu.pt")

def detect_objects(file):
    # Đọc ảnh từ file dạng bytes → PIL → numpy
    image = Image.open(file.stream).convert("RGB")
    image_np = np.array(image)

    # Nhận diện đối tượng
    results = model(image_np)

    # Trích xuất tên các object
    labels = results.names
    detected_objects = results[0].boxes.cls.tolist()
    names = [labels[int(cls)] for cls in detected_objects]

    return {"objects": names}