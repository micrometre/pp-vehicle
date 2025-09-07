.PHONY: infer-demo
infer-demo: 
	python -u tools/infer.py -c configs/ppvehicle/vehicle_yolov3/vehicle_yolov3_darknet.yml \
		-o weights=https://paddledet.bj.bcebos.com/models/vehicle_yolov3_darknet.pdparams \
		use_gpu=false \
		--infer_dir configs/ppvehicle/vehicle_yolov3/demo \
		--draw_threshold 0.2 \
		--output_dir output