install:
	@echo "Installing nanocamera..."
	pip install nanocamera

detect: install
	@echo "Predicting camera live stream..."
	(cd yolov5_csi && python3 detect_modified.py --source 3 --weights weights/yolov5_custom_ds3.pt)
