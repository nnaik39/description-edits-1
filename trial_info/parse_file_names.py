import json 
import os 

f = open('pilot_exp.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
cwd = '/Users/nanditanaik/description-editing-study/'

for i in data['images']:
    if (not os.path.exists(cwd + '/' + i['filename'])):
        print("Doesn't exist: ", i['filename'])