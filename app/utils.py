from ultralytics import YOLO

# Dùng mô hình nhẹ nhất và tương thích tốt
model = YOLO("yolov5nu.pt")

def detect_objects(image_path):
    results = model(image_path)
    names = model.names

    # Lấy tên các object đã detect (duy nhất, không lặp)
    detected = set()
    for r in results:
        for c in r.boxes.cls:
            detected.add(names[int(c)])

    return list(detected)
