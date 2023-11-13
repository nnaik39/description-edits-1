import json 
import os 

#f = open('pilot_exp.json')
 
# returns JSON object as
# a dictionary
#pilot_exp = json.load(f)
 
# Iterating through the json
# list

# Open this here
f = open('description-editing-final-export.json')
study_info = json.load(f)

count_image_descriptions = {}
new_pilot_exp = {}
new_pilot_exp['images'] = []

for participant in study_info:
    for trial in study_info[participant]:
        if (trial['picture'] not in count_image_descriptions):
            count_image_descriptions[trial['picture']] = 0
        count_image_descriptions[trial['picture']] += 1
        if (trial['comments'] != ''):
            print(trial['comments'])
        if (trial['glb_comments'] != ''):
            print(trial['glb_comments'])

exit()
        
for i in pilot_exp['images']:
    if (i['filename'] in count_image_descriptions and count_image_descriptions[i['filename']] >= 3):
        print("Image ", i['filename'])
    else:
        new_pilot_exp['images'].append(i)

# If it's seen 3 times, then take it out from pilot_exp.json
# And then push pilot_exp.json!!!
json_object = json.dumps(new_pilot_exp, indent=4)
 
# Writing to sample.json
with open("new_pilot_exp.json", "w") as outfile:
    outfile.write(json_object)
