import glob, os
# directory obj is in data folder of darknet which contains both images and labels
current_dir = "obj"
# Directory where the data will reside, relative to 'darknet.exe'
path_data = 'data/obj/'
# Percentage of images to be used for the testset
percentage_test = 10;
# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')
# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  

for i in range(2,237):
    if counter == index_test:
        counter = 1
        file_test.write(path_data + "{0}".format(i) + '.jpg' + "\n")
    else:
        file_train.write(path_data + "{0}".format(i) + '.jpg' + "\n")
        counter = counter + 1
