#!/usr/bin/env python3
"""
Cleanup script to reduce PaddleDetection project to only ppvehicle-related files
"""

import os
import shutil
from pathlib import Path

def main():
    base_dir = Path("/home/ubuntu/repos/ppvehicle/PaddleDetection")
    
    # Files and directories to KEEP (everything else will be removed)
    keep_items = {
        # Essential root files
        "README.md",
        "LICENSE", 
        "requirements.txt",
        "setup.py",
        ".gitignore",
        
        # Core package - keep entire ppdet directory
        "ppdet",
        
        # Essential tools
        "tools/infer.py",
        "tools/train.py", 
        "tools/eval.py",
        "tools/export_model.py",
        
        # ppvehicle configs
        "configs/ppvehicle",
        "configs/runtime.yml",
        
        # Required base configs for yolov3
        "configs/datasets",
        "configs/yolov3",
        
        # Demo images that were used in inference
        "demo",
        
        # Keep any dataset directory if it exists
        "dataset",
        
        # Git directory
        ".git"
    }
    
    print("Starting cleanup to reduce project to ppvehicle-only files...")
    print(f"Working directory: {base_dir}")
    
    # Get all items in the base directory
    all_items = [item for item in base_dir.iterdir() if item.name != "cleanup_for_ppvehicle.py"]
    
    removed_count = 0
    kept_count = 0
    
    for item in all_items:
        item_name = item.name
        relative_path = str(item.relative_to(base_dir))
        
        # Check if this item should be kept
        should_keep = False
        for keep_pattern in keep_items:
            if relative_path.startswith(keep_pattern) or item_name == keep_pattern:
                should_keep = True
                break
        
        if should_keep:
            print(f"KEEPING: {relative_path}")
            kept_count += 1
        else:
            print(f"REMOVING: {relative_path}")
            try:
                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    item.unlink()
                removed_count += 1
            except Exception as e:
                print(f"Error removing {relative_path}: {e}")
    
    # Now clean up specific subdirectories
    configs_dir = base_dir / "configs"
    if configs_dir.exists():
        print("\nCleaning up configs directory...")
        for config_item in configs_dir.iterdir():
            if config_item.name not in ["ppvehicle", "runtime.yml", "datasets", "yolov3"]:
                print(f"REMOVING CONFIG: {config_item.relative_to(base_dir)}")
                try:
                    if config_item.is_dir():
                        shutil.rmtree(config_item)
                    else:
                        config_item.unlink()
                    removed_count += 1
                except Exception as e:
                    print(f"Error removing {config_item}: {e}")
    
    # Clean up tools directory to keep only essential tools
    tools_dir = base_dir / "tools"
    if tools_dir.exists():
        print("\nCleaning up tools directory...")
        essential_tools = ["infer.py", "train.py", "eval.py", "export_model.py"]
        for tool_item in tools_dir.iterdir():
            if tool_item.name not in essential_tools:
                print(f"REMOVING TOOL: {tool_item.relative_to(base_dir)}")
                try:
                    if tool_item.is_dir():
                        shutil.rmtree(tool_item)
                    else:
                        tool_item.unlink()
                    removed_count += 1
                except Exception as e:
                    print(f"Error removing {tool_item}: {e}")
    
    print(f"\nCleanup completed!")
    print(f"Items kept: {kept_count}")
    print(f"Items removed: {removed_count}")
    
    # Create a minimal README for the reduced project
    readme_content = """# PaddleDetection - PPVehicle Only

This is a reduced version of PaddleDetection containing only the files needed for PPVehicle functionality.

## Usage

Run vehicle detection inference:
```bash
python -u tools/infer.py -c configs/ppvehicle/vehicle_yolov3/vehicle_yolov3_darknet.yml \\
                         -o weights=https://paddledet.bj.bcebos.com/models/vehicle_yolov3_darknet.pdparams \\
                            use_gpu=false \\
                         --infer_dir configs/ppvehicle/vehicle_yolov3/demo \\
                         --draw_threshold 0.2 \\
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
"""
    
    with open(base_dir / "README_PPVEHICLE.md", "w") as f:
        f.write(readme_content)
    
    print("Created README_PPVEHICLE.md with usage instructions.")

if __name__ == "__main__":
    main()
