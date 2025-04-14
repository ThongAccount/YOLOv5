from ultralytics import YOLO
from PIL import Image
import numpy as np

# Dùng mô hình nhẹ nhất và tương thích tốt
model = YOLO("yolov5nu.pt")

def detect_objects(image_path):
    results = model(image_path)

    # model.names chứa dict tên các class
    names = model.names

    # Vì results là list, lặp qua từng result
    objects = []
    for r in results:
        if hasattr(r, "boxes") and r.boxes is not None:
            for c in r.boxes.cls:
                label = names[int(c)]
                if label not in objects:
                    objects.append(label)
    return objects
