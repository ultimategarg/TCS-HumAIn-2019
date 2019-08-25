# Object detection & OCR:
Vehicle Number Plate detection -  Identify the license place in the image and do an OCR to extract the characters from the detected license plate
## steps:
1. At first,we run a python script `download.py` to download all the images in a specific folder `dataset` provided in data `Indian_Number_plates.json`.There are total 237 images in dataset. 
1. Use BBox-Label-Tool for annotating the data or use the python script to extract the bounding box coordinates from data `Indian_Number_plates.json'.. 
1. YOLOv2 needs files in the following format: so again run a python script to store data in labels_new folder.
  `|category number| |object center in X| |object center in Y| |object width in X| |object width in Y|`
  
  
  
