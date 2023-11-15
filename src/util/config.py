import os

EPOCHS_COUNT = 3

RANDOM_STATE = 42

ASSETS_FOLDER_PATH = os.path.join(
    os.path.dirname(__file__), os.pardir, "assets")

IMAGE_FOLDER_PATH = os.path.join(ASSETS_FOLDER_PATH, "img")
YML_DATASET_PATH = os.path.join(ASSETS_FOLDER_PATH, "yolo_yaml")

PRETRAINED_MODEL_PATH = os.path.join(ASSETS_FOLDER_PATH, "pretrained_models")
