## Introduction

Head injuries pose a significant risk in workplaces, with approximately 1,000 worker deaths reported annually by the Occupational Safety and Health Administration (OSHA). Regrettably, 84% of these fatal head injuries occur among employees who were not wearing head protection at the time of the incident. 

It is of paramount importance to ensure the safety of workers in workplaces, especially in industrial and construction settings. One way to do this is by enforcing the use of safety helmets, which can help prevent serious head injuries caused by falling objects or other hazards.

However, manual monitoring of workers wearing helmets could be challenging and non-sustainable in large scale settings. Therefore,  this project aims to build a computer vision model that can detect whether a worker is wearing a safety helmet.  The model could be used to integrate with existing surveillance systems and automate the inspection process. 


## Related Works
- CNN-based model for detecting safety helmets in images
- different versions of YOLO for object detection

## Data Exploration
- where are the datasets from
- explorations of the datasets

## Methods
- use CoLab to train the model, as it is free and has GPU support
- test on a small subset of the dataset
- Image Dataset Augmentation

## Model and Performance Evaluation
- TODO

## Deployment to Jetson Nano
- Challenge of Jetpack version
  - at the expense of losing the ability to use sparkfun's libraries


## Results
- TODO

## Discussions and Insights
- TODO


## Resume training
https://github.com/ultralytics/yolov5/issues/7456
https://github.com/ultralytics/yolov5/issues/6419
https://github.com/ultralytics/yolov5/issues/1353
https://stackoverflow.com/questions/71902562/how-to-resume-continue-from-already-trained-yolo5-training-epoch
https://github.com/ultralytics/yolov5/wiki/Tips-for-Best-Training-Results