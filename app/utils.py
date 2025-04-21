import torch, cv2, time
import numpy as np
from app.yolov5_lite.models.common import DetectMultiBackend
from app.yolov5_lite.utils.general import non_max_suppression, scale_coords
from app.yolov5_lite.utils.dataloaders import letterbox

# Global variables
device = 'cpu'
model = None
stride = None
names = None

def load_model(model_path='model/yolov5n.pt'):
    global model, stride, names
    model = DetectMultiBackend(model_path, device=device)
    stride = model.stride
    names = model.names
    print("✅ Model loaded!")

def detect_objects(image_bytes):
    global model, stride, names, device
    start_time = time.time()

    # Convert bytes to OpenCV image
    nparr = np.frombuffer(image_bytes, np.uint8)
    img0 = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Preprocess
    t1 = time.time()
    img = letterbox(img0, 640, stride=stride)[0]
    img = img.transpose((2, 0, 1))[::-1]
    img = np.ascontiguousarray(img)
    img = torch.from_numpy(img).to(device).float() / 255.0
    if img.ndimension() == 3:
        img = img.unsqueeze(0)
    print(f"[🧠 Preprocess] {(time.time() - t1):.2f}s")

    # Inference
    t2 = time.time()
    pred = model(img, augment=False, visualize=False)
    pred = non_max_suppression(pred)[0]
    print(f"[⚙️ Inference] {(time.time() - t2):.2f}s")

    # Postprocess
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
