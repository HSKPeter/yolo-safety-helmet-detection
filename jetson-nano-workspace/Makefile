upgrade-pip:
	@echo "Upgrading pip..."
	pip3 install --upgrade pip

install: upgrade-pip
	@echo "Installing nanocamera..."
	pip3 install nanocamera

detect: install
	@echo "Predicting camera live stream..."
	(cd yolov5_csi && python3 detect_modified.py --source 3 --weights weights/yolov5_custom_ds3_35.pt)