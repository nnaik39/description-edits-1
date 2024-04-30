import json
import os 

f = open('old_context_assignments.json')
data = json.load(f)
import shutil

folder_path = 'commvqa_new_images/'

# TODO: Practice automatically moving!

for i in data:
    image = i['filename'].replace('images/', '')

    if (os.path.isfile(folder_path + image)):
        shutil.move(folder_path + image, 'described_images/' + image)

print(len([name for name in os.listdir('described_images/') if os.path.isfile(name)]))
