# Automated Road Damage Detection

![YOLOv5](https://img.shields.io/badge/-YOLOv5-brightgreen)
![YOLOv8](https://img.shields.io/badge/-YOLOv8-brightgreen)


An advanced deep learning project for automated detection and classification of road damages using YOLOv5 and YOLOv8 models. The system can detect various types of road damages including longitudinal cracks, transverse cracks, alligator cracks, potholes, and more.

## Features

- Real-time road damage detection
- Support for multiple damage types:
  - Longitudinal cracks
  - Transverse cracks
  - Alligator cracks
  - Potholes
  - Manhole covers
  - Longitudinal patches
  - Transverse patches
- Integration with both YOLOv5 and YOLOv8 architectures
- Image augmentation support for improved model training
- Data splitting utilities for dataset preparation
- Flexible model training and evaluation pipelines


### Prerequisites

- Python 3.8 or higher
- CUDA-capable GPU (recommended for training)
- PyTorch
- Other dependencies as listed in `requirements.txt`

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Navneeth-Krishna/AutomatedRoadDamageDetection.git
cd AutomatedRoadDamageDetection
```

2. Install the required dependencies:
```bash
pip install -r Yolov5/requirements.txt
```

3. Prepare your dataset:
- Organize your images in the following structure:
  ```
  images/
  ├── train/
  ├── val/
  └── test/
  ```
- Update `data.yaml` with your dataset paths and class names

### Usage

#### Training

To train the model on your dataset:

```bash
# For YOLOv5
python Yolov5/train.py --img 640 --batch 16 --epochs 100 --data data.yaml --weights yolov5s.pt

# For YOLOv8
# Use the yolov8s.pt weights and follow YOLOv8 training conventions
```

#### Data Splitting

Use the provided Split.py utility to prepare your dataset:

```bash
python Split.py
```

## Model Performance

The system uses state-of-the-art YOLO architectures:
- YOLOv5: Fast and accurate object detection
- YOLOv8: Latest improvements in the YOLO family


## Author

[Navneeth Krishna Aravind](https://github.com/Navneeth-Krishna)
