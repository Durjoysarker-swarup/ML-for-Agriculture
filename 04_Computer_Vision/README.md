# Computer Vision

Overview

This directory contains notebooks and examples for computer vision tasks in agriculture: crop/disease detection, segmentation, plant counting, and remote-sensing image analysis.

What's included
- Image preprocessing utilities, data augmentation recipes, transfer learning examples (ResNet, EfficientNet), and segmentation demos.
- Evaluation notebooks showing confusion matrices, mAP calculations, and IoU for segmentation tasks.

Prerequisites
- Python 3.8+ and the libraries in `requirements.txt`.
- For model training, a CUDA-enabled GPU is recommended. Include smaller demo datasets for CPU-only environments.

How to run
1. Install dependencies and, optionally, GPU drivers for CUDA/cuDNN when training larger models.
2. Put image datasets under `data/images/` or update dataset paths in the notebooks.
3. Start Jupyter and run the notebooks; check the `TRAINING_NOTE` cell for long-running steps.

Dataset guidelines
- Keep directory structure consistent: `data/images/train`, `data/images/val`, `data/images/test`, and annotation files in COCO/PASCAL/CSV formats as used in the notebook.
- Provide script(s) to convert custom annotations into the required format used by the notebooks.

Modeling tips
- Use transfer learning and freeze early layers for small datasets.
- Use appropriate augmentations (color jitter, random crops, flips) but preserve the semantics for plant disease images.

Contributing
- Document dataset sources, expected annotation schema, and any licensing restrictions for imagery.