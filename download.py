import urllib.request
import json
#f = open('Indian_Number_plates.json')
data = [json.loads(line) for line in open('Indian_Number_plates.json', 'r')]
i=0
for k in data:
         urllib.request.urlretrieve(k['content'], "img{0}".format(i)+".jpg")
         i=i+1
