from ultralytics import YOLO

model = YOLO("yolov8n.pt")

video_path = "data/match.mov"

results = model.predict(
    source = video_path,
    save = True,
    project = "./data/output",
    name = "detection",
    conf = 0.3,
    iou = 0.5,
    classes = [0, 32]
)