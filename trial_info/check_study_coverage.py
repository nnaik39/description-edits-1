'''
This file checks coverage of questions in the experiment, saves all completed datapoints to a new file, and fills 'new_pilot_exp.json'
with the datapoints that have yet to be covered.
'''

import json
from math import e

f = open('/Users/nanditanaik/Downloads/ig-vqa-default-rtdb-description-editing-1000-images-expansion-export (6).json')
study_info = json.load(f)

f = open('old_context_assignments.json')
context_assignments = json.load(f)

questions_per_image_context_pair = {}
new_pilot_exp = {}
new_pilot_exp['images'] = []

f = open('pilot_exp.json')
pilot_exp = json.load(f)

answers = {}
collected_datapoints = []

start_description_per_image = {}

for i in context_assignments:
    found_in_pilot_exp = False

    for participant in study_info:
        for trial in study_info[participant]:
            if (trial['picture'] == i['filename']):
                found_in_pilot_exp = True

    if (not found_in_pilot_exp):
        if ({'filename': i['filename'],
            'description': i['description']} not in new_pilot_exp['images']):
                new_pilot_exp['images'].append({
                    'filename': i['filename'],
                    'description': i['description']
            })
            
#with open("new_pilot_exp.json", "w") as outfile:
 #   outfile.write(json.dumps(new_pilot_exp, indent = 4))

for participant in study_info:
    for trial in study_info[participant]:
        found_in_pilot_exp = False 

        if (trial['comments'] != ''):
            print("Comments: ", trial['comments'])
        if (trial['glb_comments'] != ''):
            print("General comments: ", trial['glb_comments'])

        for pilot_exp_entry in pilot_exp['images']:
            if (trial['picture'] == pilot_exp_entry['filename']):
                found_in_pilot_exp = True
        
        if (found_in_pilot_exp):
            if (((trial['picture'])) not in answers):
                answers[(trial['picture'])] = []
            answers[(trial['picture'])].append((trial['final_description']))

            if (trial['picture'] not in start_description_per_image):
                start_description_per_image[trial['picture']] = trial['start_description']

answers_so_far = []
for image in answers:
    i = {'image': image, 'answers': answers[(image)]}

    answers_so_far.append(i)

    if (len(answers[(image)]) >= 2):
        i = {
            'image': image,
            'answers': answers[(image)]}
        collected_datapoints.append(i)
    else:
        new_pilot_exp['images'].append({
            'filename': image,
            'description': start_description_per_image[image]
        })

print("Number of datapoints left for full coverage: ", len(new_pilot_exp['images']))
print("Total number of descriptions seen: ", len(answers))
print("number of images seen: ", len(answers_so_far))

with open("new_pilot_exp.json", "w") as outfile:
    outfile.write(json.dumps(new_pilot_exp, indent = 4))

with open("collected_description_datapoints.json", "w") as outfile:
    outfile.write(json.dumps(collected_datapoints, indent = 4))

with open('answers_so_far.json', 'w') as outfile:
    outfile.write(json.dumps(answers_so_far, indent = 4))