from ultralytics import YOLO
import os

from util.config import EPOCHS_COUNT, IMAGE_FOLDER_PATH, YML_DATASET_PATH

def main():
    print("Loading pretrained YOLOv8 model...")
    current_dir = os.path.dirname(os.path.realpath(__file__))
    path_of_pretrained_model = os.path.join(current_dir, "yolov8n.pt")
    model = YOLO(path_of_pretrained_model)
    print("Loaded pretrained YOLOv8 model.")

    # Train the model using the 'coco8.yaml' dataset for 3 epochs
    yaml_file_name = "coco8.yaml"
    print(f"Training model with {yaml_file_name} dataset...")
    yaml_file_path = os.path.join(YML_DATASET_PATH, yaml_file_name)
    results = model.train(data=yaml_file_path, epochs=EPOCHS_COUNT)

    # Evaluate the model's performance on the validation set
    print("Evaluating model...")
    results = model.val()

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
