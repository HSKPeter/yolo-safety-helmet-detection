import torch
import os

from util.config import IMAGE_FOLDER_PATH, CUSTOM_MODEL_PATH

def main():
    custom_yolo_v5_model_path = os.path.join(CUSTOM_MODEL_PATH, "yolov5_custom_ds3_35.pt")

    model = torch.hub.load('ultralytics/yolov5', 'custom', path=custom_yolo_v5_model_path)
    model.conf = 0.2
    LABEL_FOR_HARDHAT = 0
    LABEL_FOR_NO_HARDHAT = 2
    LABEL_FOR_PERSON = 5
    model.classes = [LABEL_FOR_HARDHAT, LABEL_FOR_NO_HARDHAT, LABEL_FOR_PERSON]

    img_path = os.path.join(IMAGE_FOLDER_PATH, "no_helmet", "no_helmet_1.jpg")
    results = model(img_path)
    
    results.show()
    results.save()


if __name__ == "__main__":
    main()
