# Dataset

3 datasets should be downloaded from Kaggle
- Dataset 1: [Construction Site Safety Image Dataset Roboflow](https://www.kaggle.com/datasets/snehilsanyal/construction-site-safety-image-dataset-roboflow)
- Dataset 2: [Safety Helmet Detection](https://www.kaggle.com/datasets/andrewmvd/hard-hat-detection/)
- Dataset 3: [HardHat-Vest Dataset](https://www.kaggle.com/datasets/muhammetzahitaydn/hardhat-vest-dataset-v3)

The dataset should be placed in the following structure:
```
├── dataset_1  (232MB)
│   ├── css-data
│   │   ├── README.dataset.txt
│   │   ├── README.roboflow.txt
│   │   ├── test
│   │   ├── train
│   │   └── valid
│   ├── results_yolov8n_100e
│   │   └── kaggle
│   └── source_files
│       └── source_files
├── dataset_2 (1.3GB)
│   ├── annotations
│   └── images
└── dataset_3 (4.4GB)
    ├── images
    │   ├── test
    │   ├── train
    │   └── val
    └── labels
        ├── classes.txt
        ├── test
        ├── train
        └── val
```