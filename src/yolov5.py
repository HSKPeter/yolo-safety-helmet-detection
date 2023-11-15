from ultralytics import YOLO
import os

from util.config import EPOCHS_COUNT, IMAGE_FOLDER_PATH, PRETRAINED_MODEL_PATH, YML_DATASET_PATH

def main():
    print("Loading pretrained YOLOv5 model...")
    pretrained_yolo_v5_model_path = os.path.join(PRETRAINED_MODEL_PATH, "yolov5nu.pt")
    model = YOLO(pretrained_yolo_v5_model_path)
    print("Loaded pretrained YOLOv5 model.")

    # Train the model using the 'coco8.yaml' dataset for 3 epochs
    yaml_file_name = "coco8.yaml"
    print(f"Training model with {yaml_file_name} dataset...")
    yaml_file_path = os.path.join(YML_DATASET_PATH, yaml_file_name)
    results = model.train(data=yaml_file_path, epochs=EPOCHS_COUNT)

    # Evaluate the model's performance on the validation set
    print("Evaluating model...")
    results = model.val()
    print(results)

    image_path = os.path.join(IMAGE_FOLDER_PATH, "bus.jpg")
    print(f"Predicting image at {image_path}...")
    # Run inference on 'bus.jpg' with arguments
    model.predict(image_path, save=True, imgsz=320, conf=0.5)    

    print("\n\nExporting model to ONNX format...")
    # Export the model to ONNX format
    success = model.export(format='onnx')    
    print(success)

if __name__ == "__main__":
    main()
