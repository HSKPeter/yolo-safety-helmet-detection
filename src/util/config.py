import os

EPOCHS_COUNT = 3

RANDOM_STATE = 42

IMAGE_FOLDER_PATH = os.path.join(
    os.path.dirname(__file__), os.pardir, "assets", "img")

YML_DATASET_PATH = os.path.join(os.path.dirname(
    __file__), os.pardir, "assets", "datasets")
