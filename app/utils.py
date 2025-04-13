from ultralytics import YOLO

# Load YOLOv5n model (rất nhẹ)
model = YOLO("yolov5n.pt")

def detect_objects(image_path):
    results = model(image_path)
    names = model.names
    object_names = set()

    for r in results:
        for cls in r.boxes.cls:
            object_names.add(names[int(cls)])

    return list(object_names)
