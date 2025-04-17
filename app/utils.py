import torch
from PIL import Image
from io import BytesIO

model = torch.hub.load('ultralytics/yolov5', 'custom', path='app/yolov5nu.pt', force_reload=True)

def detect_objects(file):
    img = Image.open(BytesIO(file.read()))
    results = model(img)
    labels = results.names
    detected = results.pred[0][:, -1].tolist()
    unique_labels = list(set([labels[int(i)] for i in detected]))
    return unique_labels
    