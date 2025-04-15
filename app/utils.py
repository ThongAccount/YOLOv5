from ultralytics import YOLO
from PIL import Image
import os

model = YOLO("yolov5nu.pt")

def convert_image_to_png(original_path):
    img = Image.open(original_path).convert("RGB")
    new_path = os.path.splitext(original_path)[0] + ".png"
    img.save(new_path, format="PNG")
    return new_path

def detect_objects(image_path):
    # Chuyển ảnh về PNG
    png_image_path = convert_image_to_png(image_path)

    # Phát hiện đối tượng
    results = model(png_image_path)

    if not results:
        return []

    result = results[0]
    names = model.names
    detected_labels = result.boxes.cls.tolist()
    unique_objects = list(set([names[int(i)] for i in detected_labels]))

    return unique_objects
