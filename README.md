# Object detection & OCR:
Vehicle Number Plate detection -  Identify the license place in the image and do an OCR to extract the characters from the detected license plate
## steps:
1. At first,we run a python script `download.py` to download all the images in a specific folder `dataset` provided in data `Indian_Number_plates.json`.There are total 237 images in dataset. 
1. Use BBox-Label-Tool for annotating the data or use the python script to extract the bounding box coordinates from data `Indian_Number_plates.json
1. Store the data to be annotated in the “001” folder of the Images directory. Now run `main.py` file.In the GUI enter “001” as the Img Dir and load the dataset from “001” folder and start annotating. 
1. YOLOv2 needs files in the following format:
  `|category number| |object center in X| |object center in Y| |object width in X| |object width in Y|`
  
  
