# PaddleDetection - PPVehicle Only

This is a reduced version of PaddleDetection containing only the files needed for PPVehicle functionality.

## Usage

Run vehicle detection inference:
```bash
python -u tools/infer.py -c configs/ppvehicle/vehicle_yolov3/vehicle_yolov3_darknet.yml \
                         -o weights=https://paddledet.bj.bcebos.com/models/vehicle_yolov3_darknet.pdparams \
                            use_gpu=false \
                         --infer_dir configs/ppvehicle/vehicle_yolov3/demo \
                         --draw_threshold 0.2 \
                         --output_dir output
```

## Contents

- `ppdet/`: Core PaddleDetection package
- `configs/ppvehicle/`: PPVehicle-specific configurations  
- `configs/yolov3/`: YOLOv3 base configurations
- `configs/datasets/`: Dataset configurations
- `tools/`: Essential tools (infer.py, train.py, eval.py, export_model.py)
- `demo/`: Demo images for testing

Original project: https://github.com/PaddlePaddle/PaddleDetection
