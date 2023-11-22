import torch
import os

from util.config import IMAGE_FOLDER_PATH, PRETRAINED_MODEL_PATH

def main():
    pretrained_yolo_v5_model_path = os.path.join(PRETRAINED_MODEL_PATH, "yolov5_custom_ds3.pt") # yolov5nu.pt yolov5_custom_ds3
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=pretrained_yolo_v5_model_path)
    img_path = os.path.join(IMAGE_FOLDER_PATH, "helmet.jpg")

    results = model(img_path)
    results.show()
    results.save()   


if __name__ == "__main__":
    main()
