import os

files = os.listdir('commvqa_new_images/')

files.sort()
files.remove('.DS_Store')
print(files[:11])