VIRTUAL_ENV_NAME="venv"

# Executables
PYTHON3_VENV_BIN_PATH := "${VIRTUAL_ENV_NAME}/bin/python3.11"
PYTHON3_VENV_PIP_PATH := "${VIRTUAL_ENV_NAME}/bin/pip3.11"

# Dataset urls
KAGGLE_DATASET_1="https://www.kaggle.com/datasets/snehilsanyal/construction-site-safety-image-dataset-roboflow"
KAGGLE_DATASET_2="https://www.kaggle.com/datasets/andrewmvd/hard-hat-detection/"
KAGGLE_DATASET_3="https://www.kaggle.com/datasets/muhammetzahitaydn/hardhat-vest-dataset-v3"

# Colors
YELLOW=\033[33m
RESET=\033[0m

all: install build run

setup: create-venv install show-setup-dataset-steps

create-venv:
	@echo "Creating virtual environment ..."
	@python3 -m venv ${VIRTUAL_ENV_NAME}

show-setup-dataset-steps:
	@echo "\n$(YELLOW)Please follow the steps below to setup the dataset:$(RESET)"
	@echo "[STEP 1] Open your browser and visit ${KAGGLE_DATASET_1} to download dataset 1"
	@echo "[STEP 2] Open your browser and visit ${KAGGLE_DATASET_2} to download dataset 2"
	@echo "[STEP 3] Open your browser and visit ${KAGGLE_DATASET_3} to download dataset 3"
	@echo "[STEP 4] Unzip the files, move them to the 'data' folder and ensure the folder structure aligns with the README guide in the 'data' folder"

install:
	@echo "Installing dependencies ..."
	@${PYTHON3_VENV_PIP_PATH} install -r requirements.txt --upgrade pip --quiet	

# Build project
build:
	@echo "Building project ..."
	@${PYTHON3_VENV_PIP_PATH} install -e . --quiet

run:
	@echo "Running project ..."
	@${PYTHON3_VENV_BIN_PATH} src/model/main.py

clean:
	@echo "Cleaning virtual environment ..."
	@rm -rf ${VIRTUAL_ENV_NAME}
	@echo "Cleaned virtual environment!"