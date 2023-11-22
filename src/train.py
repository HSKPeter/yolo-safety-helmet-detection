from ultralytics import YOLO
import os

from util.config import EPOCHS_COUNT, PRETRAINED_MODEL_PATH

def main():
    print("Loading pretrained YOLOv5 model...")
    pretrained_yolo_v5_model_path = os.path.join(PRETRAINED_MODEL_PATH, "yolov5nu.pt")
    model = YOLO(pretrained_yolo_v5_model_path)
    print("Loaded pretrained YOLOv5 model.")

    yaml_file_path = os.path.join("assets", "yolo_yaml", "dataset_1.yaml")
    print(f"Training model with {yaml_file_path} dataset...")
    results = model.train(data=yaml_file_path, epochs=EPOCHS_COUNT) 
    print(results)

    print("\n\nExporting model to PyTorch format...")
    # Export the model to ONNX format
    success = model.export(format='pt')
    print(success)

if __name__ == "__main__":
    main()
