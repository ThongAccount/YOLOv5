<<<<<<< HEAD
import sys
import torch

# Add yolov5 repo to path
sys.path.insert(0, 'app/yolov5')

from models.common import DetectMultiBackend
from utils.datasets import letterbox
from utils.general import non_max_suppression, scale_coords
from utils.torch_utils import select_device
import cv2
import numpy as np

device = select_device('')
model = DetectMultiBackend('app/yolov5nu.pt', device=device)
model.eval()

def detect_objects(image_np):
    img = letterbox(image_np, 640, stride=32, auto=True)[0]
    img = img.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
    img = np.ascontiguousarray(img)

    img_tensor = torch.from_numpy(img).to(device).float()
    img_tensor /= 255.0
    if img_tensor.ndimension() == 3:
        img_tensor = img_tensor.unsqueeze(0)

    pred = model(img_tensor, augment=False, visualize=False)
    pred = non_max_suppression(pred, 0.25, 0.45, classes=None, agnostic=False)

    class_names = model.names
    results = []

    for det in pred:
        if len(det):
            for *xyxy, conf, cls in det:
                results.append(class_names[int(cls)])

    return list(set(results))  # loại trùng
=======
from ultralytics import YOLO
from PIL import Image
import os

try:
    model = YOLO("app/models/yolov5nu.pt")
    print("✅ Model loaded OK!")
except Exception as e:
    print("❌ Error loading model:", e)

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
>>>>>>> parent of b2839bf (l)
