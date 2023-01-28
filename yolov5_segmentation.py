# -*- coding: utf-8 -*-
"""Copy of Yolov5_segmentation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eIS8R8-WNO2ZTx9InoMbpMQvIPo_dKFY
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive

# Commented out IPython magic to ensure Python compatibility.
# %mkdir YOLOv5

# Commented out IPython magic to ensure Python compatibility.
# %cd YOLOv5

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/ultralytics/yolov5.git
# %cd yolov5 
# %pip install -r requirements.txt

import torch
import utils
display =utils.notebook_init()

!pip install roboflow

"""from roboflow import Roboflow
rf = Roboflow(api_key="") # You will get your own key for download link from roboflow
project = rf.workspace("myworkspace-l4whl").project("yolov7_inst_seg")
dataset = project.version(1).download("yolov5")"""

dataset.location

!python /content/drive/MyDrive/YOLOv5/yolov5/segment/train.py --img 320 --batch 120 --epochs 50 --data /content/drive/MyDrive/YOLOv5/yolov5/Yolov7_inst_seg-1/data.yaml --weights yolov5s-seg.pt

