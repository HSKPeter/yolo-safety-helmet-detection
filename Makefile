SHELL := $(shell which bash)
ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

VIRTUAL_ENV_NAME="venv"

# From https://gist.github.com/sighingnow/deee806603ec9274fd47
OSFLAG 				:=
ifeq ($(OS),Windows_NT)
	OSFLAG = WIN32
else
	UNAME_S := $(shell uname -s)
	ifeq ($(UNAME_S),Linux)
		OSFLAG = LINUX
	endif
	ifeq ($(UNAME_S),Darwin)
		OSFLAG = OSX
	endif
endif

# Executables
PYTHON3_VENV_BIN_PATH := "${ROOT_DIR}/${VIRTUAL_ENV_NAME}/bin/python3.11"
PYTHON3_VENV_PIP_PATH := "${ROOT_DIR}/${VIRTUAL_ENV_NAME}/bin/pip3.11"

# Dataset urls
KAGGLE_DATASET_1="https://www.kaggle.com/datasets/snehilsanyal/construction-site-safety-image-dataset-roboflow"
KAGGLE_DATASET_2="https://www.kaggle.com/datasets/andrewmvd/hard-hat-detection/"
KAGGLE_DATASET_3="https://www.kaggle.com/datasets/muhammetzahitaydn/hardhat-vest-dataset-v3"

# Colors
YELLOW=\033[33m
RESET=\033[0m

setup: create-venv install show-setup-dataset-steps

create-venv:
	@echo "Creating virtual environment ..."
	@python3 -m venv ${VIRTUAL_ENV_NAME}

show-setup-dataset-steps:
	@echo "\n$(YELLOW)Please follow the steps below to setup the dataset:$(RESET)"
	@echo "[STEP 1] Open your browser and visit ${KAGGLE_DATASET_1} to download dataset 1"
	@echo "[STEP 2] Open your browser and visit ${KAGGLE_DATASET_2} to download dataset 2"
	@echo "[STEP 3] Open your browser and visit ${KAGGLE_DATASET_3} to download dataset 3"
	@echo "[STEP 4] Unzip the files, move them to the 'src/assets/datasets' folder and ensure the folder structure aligns with the README guide in that folder"

install:
	@echo "Installing dependencies ..."
	@${PYTHON3_VENV_PIP_PATH} install -r requirements.txt --upgrade pip --quiet	
	@$(MAKE) install-pytorch
	@echo "Installing dependencies for submodules ..."
	@${PYTHON3_VENV_PIP_PATH} install -r src/submodules/yolov5/requirements.txt --quiet

# From https://pytorch.org/get-started/locally/
install-pytorch:
ifeq ($(OSFLAG),LINUX)
	@echo "Installing PyTorch for Linux ..."
endif

ifeq ($(OSFLAG),OSX)
	@echo "Installing PyTorch for OSX ..."
	@${PYTHON3_VENV_PIP_PATH} install torch torchvision torchaudio --quiet
endif

ifeq ($(OSFLAG),WIN32)
	@echo "Installing PyTorch for Windows ..."
	@${PYTHON3_VENV_PIP_PATH} install torch torchvision torchaudio --quiet
endif
	
# Build project
build:
	@echo "Building project artifacts ..."
	@${PYTHON3_VENV_PIP_PATH} install -e . --quiet

yolo: build
	@echo "Running demo of YOLOv5 with coco8 dataset ..."
	@${PYTHON3_VENV_BIN_PATH} src/yolov5.py

train: build
	@echo "Training custom YOLO model"
	@(cd src && ${PYTHON3_VENV_BIN_PATH} train.py)

camera-detect:
	@echo "Running detection on webcam ..."
	@(cd src/submodules/yolov5 && ${PYTHON3_VENV_BIN_PATH} detect.py --source 0 --nosave)
	
clean-venv:
	@echo "Cleaning virtual environment ..."
	@rm -rf ${VIRTUAL_ENV_NAME}
	@echo "Cleaned virtual environment!"

clean-runs:
	@echo "Cleaning runs folder ..."
	@rm -rf runs
	@echo "Cleaned runs folder!"

clean: clean-venv clean-runs
	@echo "Cleaned project!"


