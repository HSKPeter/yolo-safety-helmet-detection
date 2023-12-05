# Jetson Nano Workspace

```
.
├── Makefile # Makefile for the project
├── README.md
├── installRealSenseSDK # Setup Intel's librealsense for the NVIDIA Jetson Developer Kits
├── yolov5 # YOLOv5 v7.0 which is compatible with Python3.6
├── yolov5_csi # Custom YOLOv5 code to use CSI camera from https://www.youtube.com/watch?v=ZXbOV83EXdQ
└── yolov5_object_mapping # Custom YOLOv5 code from https://www.youtube.com/watch?v=oKaLyow7hWU
```

- Run `make detect` to run the YOLOv5 object detection on the Jetson Nano with CSI camera