from ultralytics import YOLO
from PIL import Image
import numpy as np

model = YOLO('yolov5nu.pt')

def detect_objects(image_file):
    # Chuyển file upload sang PIL
    image = Image.open(image_file.stream).convert("RGB")
    image_np = np.array(image)

    results = model(image_np)
    names = model.names

    objects = []
    for r in results:
        if hasattr(r, "boxes") and r.boxes is not None:
            for c in r.boxes.cls:
                label = names[int(c)]
                if label not in objects:
                    objects.append(label)
    return objects
