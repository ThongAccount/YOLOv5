from ultralytics import YOLO
import torch
import torch
from torch.serialization import add_safe_globals
from ultralytics.nn.tasks import DetectionModel

# Load YOLOv5nu model (rất nhẹ)
add_safe_globals([DetectionModel])
model = YOLO("yolov5nu.pt")

# Tải lại mô hình với weights_only=False để xử lý vấn đề unpickling
model.model = torch.load("yolov5nu.pt", map_location="cpu", weights_only=False)

def detect_objects(image_path):
    results = model(image_path)
    names = model.names
    object_names = set()

    for r in results:
        for cls in r.boxes.cls:
            object_names.add(names[int(cls)])

    return list(object_names)
