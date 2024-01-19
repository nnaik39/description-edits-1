'''
This file checks coverage of questions in the experiment, saves all completed datapoints to a new file, and fills 'new_pilot_exp.json'
with the datapoints that have yet to be covered.
'''

import json
from math import e 

f = open('ig-vqa-default-rtdb-description-editing-final-export.json')
study_info = json.load(f)

questions_per_image_context_pair = {}
new_pilot_exp = {}
new_pilot_exp['images'] = []

f = open('pilot_exp.json')
pilot_exp = json.load(f)

answers = {}
collected_datapoints = []

for participant in study_info:
    for trial in study_info[participant]:
        found_in_pilot_exp = False 
        for pilot_exp_entry in pilot_exp['images']:
            if (trial['picture'] == pilot_exp_entry['filename']):
                    found_in_pilot_exp = True
        
        if (found_in_pilot_exp):
            if (((trial['picture'], trial['category'], trial['start_description'])) not in answers):
                answers[(trial['picture'], trial['category'], trial['start_description'])] = []
            answers[(trial['picture'], trial['category'], trial['start_description'])].append((trial['picture'], trial['category'], trial['start_description']))

for (image, context, description) in answers:
    if (len(answers[(image, context, description)]) >= 3):
        i = {
            'image': image,
            'context': context,
            'answers': answers[(image, context, description)]}
        collected_datapoints.append(i)
    else:
        new_pilot_exp['images'].append({
            'filename': image,
            'category': context,
            'description': description
        })

with open("new_pilot_exp.json", "w") as outfile:
    outfile.write(json.dumps(new_pilot_exp, indent = 4))

print("Number of collected description edits: ", len(collected_datapoints))

with open("collected_description_datapoints.json", "w") as outfile:
    outfile.write(json.dumps(collected_datapoints, indent = 4))