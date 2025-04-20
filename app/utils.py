import torch
import cv2
import numpy as np
from app.yolov5_lite.models.common import DetectMultiBackend
from app.yolov5_lite.utils.general import non_max_suppression, scale_coords
from app.yolov5_lite.utils.dataloaders import letterbox

# Khởi tạo model chỉ 1 lần
DEVICE = 'cpu'
MODEL_PATH = 'model/yolov5nu.pt'
_model = DetectMultiBackend(MODEL_PATH, device=DEVICE)
_stride, _names = _model.stride, _model.names

def detect_objects(image_bytes: bytes):
    # 1. Decode bytes thành OpenCV image
    nparr = np.frombuffer(image_bytes, np.uint8)
    img0 = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img0 is None:
        # không decode được, trả về list rỗng
        return []

    # 2. Resize & pad theo letterbox
    img = letterbox(img0, 640, stride=_stride)[0]
    # BGR→RGB, HWC→CHW, to tensor
    img = img[:, :, ::-1].transpose(2, 0, 1)
    img = np.ascontiguousarray(img)
    img = torch.from_numpy(img).to(DEVICE).float() / 255.0
    if img.ndimension() == 3:
        img = img.unsqueeze(0)

    # 3. Inference
    pred = _model(img, augment=False, visualize=False)
    pred = non_max_suppression(pred)[0]

    # 4. Post-process
    results = []
    if pred is not None and len(pred):
        pred[:, :4] = scale_coords(img.shape[2:], pred[:, :4], img0.shape).round()
        for *xyxy, conf, cls in pred:
            results.append(_names[int(cls)])
    # trả về danh sách unique
    return list(set(results))
