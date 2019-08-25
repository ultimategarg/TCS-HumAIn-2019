# Object detection & OCR:
Vehicle Number Plate detection -  Identify the license place in the image and do an OCR to extract the characters from the detected license plate

## steps:
1. At first,we run a python script `download.py` to download all the images in a specific folder `dataset` provided in data `Indian_Number_plates.json`.There are total 237 images in dataset. 
1. Use the python script to extract the bounding box coordinates from data `Indian_Number_plates.json' labels_new folder
1. YOLOv2 needs files in the following format:</br>
  `|category number| |object center in X| |object center in Y| |object width in X| |object width in Y|`
1. Now make a directory with both images and labels(.txt).Create an “obj” folder in the “data” directory of the darknet and store these images and labels in the “obj” folder.
1. To create train.txt and test.txt files we run a python file `train_test_split.py

## Configuration files preparation:
You need to create following three files in the “cfg” directory.

- obj.data
- obj.names
- yolo-voc.2.0.cfg


**Training**:
Before starting training, you need to download the pre-trained weights.<br/>
`darknet.exe detector train cfg/obj.data cfg/yolo-voc.2.0.cfg darknet19_448.conv.23`
  
  
  
