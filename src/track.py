from ultralytics import YOLO
import os

model = YOLO("yolov8n.pt")

output_dir = os.path.abspath("data/output")

results = model.track(
    source = "data/input/match.mov",
    save = True,
    project = output_dir,
    name = "tracking",
    conf = 0.3,
    iou = 0.5,
    classes = [0],
    tracker = "bytetrack.yaml"
)