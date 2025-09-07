# PaddleDetection - PPVehicle Edition

This is a streamlined version of PaddleDetection focused specifically on vehicle detection using PPVehicle models. This reduced version contains only the essential components needed for vehicle detection inference, training, and evaluation.

**Original PaddleDetection**: PaddleDetection is an end-to-end object detection development toolkit based on PaddlePaddle.

## Quick Start - Vehicle Detection

Run vehicle detection inference on CPU:
```bash
python -u tools/infer.py -c configs/ppvehicle/vehicle_yolov3/vehicle_yolov3_darknet.yml \
                         -o weights=https://paddledet.bj.bcebos.com/models/vehicle_yolov3_darknet.pdparams \
                            use_gpu=false \
                         --infer_dir configs/ppvehicle/vehicle_yolov3/demo \
                         --draw_threshold 0.2 \
                         --output_dir output
```

## Contents

This reduced version contains:

- **Core Package**: `ppdet/` - Complete PaddleDetection core package
- **PPVehicle Configs**: `configs/ppvehicle/` - Vehicle-specific configurations  
- **YOLOv3 Base**: `configs/yolov3/` - YOLOv3 base configurations required by PPVehicle
- **Dataset Config**: `configs/datasets/` - Dataset configurations
- **Runtime Config**: `configs/runtime.yml` - Runtime configurations
- **Essential Tools**: 
  - `tools/infer.py` - Inference tool
  - `tools/train.py` - Training tool
  - `tools/eval.py` - Evaluation tool  
  - `tools/export_model.py` - Model export tool
- **Demo Data**: `demo/` - Sample images for testing
- **Datasets**: `dataset/` - Dataset directory structure

## Features

- Vehicle detection with YOLOv3 architecture
- CPU and GPU inference support
- Model training and evaluation capabilities
- Multiple vehicle types classification (6 classes)
- Easy-to-use inference API

## Installation

```bash
pip install -r requirements.txt
pip install -e .
```

## License

This project is released under the [Apache 2.0 license](LICENSE).

## Original Project

Original PaddleDetection: https://github.com/PaddlePaddle/PaddleDetection

This reduced version focuses specifically on PPVehicle functionality while maintaining the original project's license and attribution.
