'''
This file checks coverage of questions in the experiment, saves all completed datapoints to a new file, and fills 'new_pilot_exp.json'
with the datapoints that have yet to be covered.
'''

import json
from math import e
from tracemalloc import start 

f = open('ig-vqa-default-rtdb-description-editing-final-export.json')
study_info = json.load(f)

questions_per_image_context_pair = {}
new_pilot_exp = {}
new_pilot_exp['images'] = []

f = open('pilot_exp.json')
pilot_exp = json.load(f)

answers = {}
collected_datapoints = []

start_description_per_image = {}

for participant in study_info:
    for trial in study_info[participant]:
        found_in_pilot_exp = False 

        for pilot_exp_entry in pilot_exp['images']:
            if (trial['picture'] == pilot_exp_entry['filename']):
                    found_in_pilot_exp = True
        
        if (found_in_pilot_exp):
            if (((trial['picture'])) not in answers):
                answers[(trial['picture'])] = []
            answers[(trial['picture'])].append((trial['final_description']))

            if (trial['picture'] not in start_description_per_image):
                start_description_per_image[trial['picture']] = trial['start_description']

print("Number of images: ", len(answers))

for image in answers:
    if (len(answers[(image)]) >= 3):
        i = {
            'image': image,
            'answers': answers[(image)]}
        collected_datapoints.append(i)
    else:
        new_pilot_exp['images'].append({
            'filename': image,
            'description': start_description_per_image[image]
        })

print("Number of datapoints left: ", len(new_pilot_exp['images']))

with open("new_pilot_exp.json", "w") as outfile:
    outfile.write(json.dumps(new_pilot_exp, indent = 4))

print("Number of collected description edits: ", len(collected_datapoints))

with open("collected_description_datapoints.json", "w") as outfile:
    outfile.write(json.dumps(collected_datapoints, indent = 4))