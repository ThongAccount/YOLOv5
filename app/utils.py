import torch
import cv2
import numpy as np
from app.yolov5_lite.models.common import DetectMultiBackend
from app.yolov5_lite.utils.general import non_max_suppression, scale_coords
from app.yolov5_lite.utils.dataloaders import letterbox

def detect_objects(image_path, model_path='model/yolov5n.pt'):
    device = 'cpu'
    model = DetectMultiBackend(model_path, device=device)
    stride, names = model.stride, model.names
    img0 = cv2.imread(image_path)
    img = letterbox(img0, 640, stride=stride)[0]
    img = img.transpose((2, 0, 1))[::-1]  # BGR to RGB
    img = np.ascontiguousarray(img)
    img = torch.from_numpy(img).to(device).float() / 255.0
    if img.ndimension() == 3:
        img = img.unsqueeze(0)

    pred = model(img, augment=False, visualize=False)
    pred = non_max_suppression(pred)[0]
    results = []
    if pred is not None and len(pred):
        pred[:, :4] = scale_coords(img.shape[2:], pred[:, :4], img0.shape).round()
        for *xyxy, conf, cls in pred:
            results.append(names[int(cls)])
    return list(set(results))
