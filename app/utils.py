import torch, cv2, time
import numpy as np
from app.yolov5_lite.models.common import DetectMultiBackend
from app.yolov5_lite.utils.general import non_max_suppression, scale_coords
from app.yolov5_lite.utils.dataloaders import letterbox

def detect_objects(image_path, model_path='model/yolov5n.pt'):
    start_time = time.time()  # ⏱️ Bắt đầu tính thời gian

    device = 'cpu'
    model = DetectMultiBackend(model_path, device=device)
    stride, names = model.stride, model.names

    t1 = time.time()
    img0 = cv2.imread(image_path)
    img = letterbox(img0, 640, stride=stride)[0]
    img = img.transpose((2, 0, 1))[::-1]
    img = np.ascontiguousarray(img)
    img = torch.from_numpy(img).to(device).float() / 255.0
    if img.ndimension() == 3:
        img = img.unsqueeze(0)
    print(f"[🧠 Preprocess] {(time.time() - t1):.2f}s")

    t2 = time.time()
    pred = model(img, augment=False, visualize=False)
    pred = non_max_suppression(pred)[0]
    print(f"[⚙️ Inference] {(time.time() - t2):.2f}s")

    t3 = time.time()
    results = []
    if pred is not None and len(pred):
        pred[:, :4] = scale_coords(img.shape[2:], pred[:, :4], img0.shape).round()
        for *xyxy, conf, cls in pred:
            results.append(names[int(cls)])
    print(f"[📝 Postprocess] {(time.time() - t3):.2f}s")

    total = time.time() - start_time
    print(f"[✅ Total time] {total:.2f}s")

    return list(set(results))
