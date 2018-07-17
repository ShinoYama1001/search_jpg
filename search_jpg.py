import os

path = "./jpg"

files = os.listdir(path)
files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]
print files_file

for item in files_file:
    if '.JPG' in item or '.jpg' in item:
        print "detected images : " + item