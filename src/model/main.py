from ultralytics import YOLO
import os

from util.config import IMAGE_FOLDER_PATH

def main():
    print("Loading pretrained YOLOv8 model...")
    current_dir = os.path.dirname(os.path.realpath(__file__))
    path_of_pretrained_model = os.path.join(current_dir, "yolov8n.pt")
    model = YOLO(path_of_pretrained_model)
    print("Loaded pretrained YOLOv8 model.")

    image_path = os.path.join(IMAGE_FOLDER_PATH, "bus.jpg")
    print(f"Predicting image at {image_path}...")
    results = model(image_path)
    print(results)

    print("\n\nExporting model to ONNX format...")
    # Export the model to ONNX format
    success = model.export(format='onnx')    
    print(success)

if __name__ == "__main__":
    main()
