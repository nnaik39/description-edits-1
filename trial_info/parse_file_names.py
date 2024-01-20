import json 
import os 
import textdistance 
import random 

algs = textdistance.algorithms

f = open('pilot_exp.json')
 
# returns JSON object as
# a dictionary
pilot_exp = json.load(f)
 
# Iterating through the json
# list

# Open this here
f = open('ig-vqa-default-rtdb-description-editing-final-export.json')
study_info = json.load(f)

f = open('old_context_assignments.json')
context_assignments = json.load(f)

count_image_descriptions = {}
new_pilot_exp = {}
new_pilot_exp['images'] = []

descriptions_per_image = {}
start_description_per_image = {}
final_description_per_image = {}
images_left = []
contexts_per_image = {}

for datapoint in context_assignments['images']:
    if (datapoint['filename'] not in contexts_per_image):
        contexts_per_image[datapoint['filename']] = []
    contexts_per_image[datapoint['filename']].append(datapoint['category'])
    
question_study_json = {}
question_study_json['images'] = []

for participant in study_info:
    for trial in study_info[participant]:
        if (trial['picture'] not in count_image_descriptions):
            count_image_descriptions[trial['picture']] = 0
        count_image_descriptions[trial['picture']] += 1
        if (trial['comments'] != ''):
            print(trial['comments'])
        if (trial['glb_comments'] != ''):
            print(trial['glb_comments'])
        if (trial['picture'] not in start_description_per_image):
            start_description_per_image[trial['picture']] = trial['start_description']

        if (trial['picture'] not in descriptions_per_image):
            descriptions_per_image[trial['picture']] = []
        descriptions_per_image[trial['picture']].append(trial['final_description'])

for image in contexts_per_image:
    descriptions_per_image[image] = [x.strip() for x in descriptions_per_image[image]]

    num_start_description = descriptions_per_image[image].count(start_description_per_image[image])

    if (num_start_description >= 2):
        final_description_per_image[image] = start_description_per_image[image]
    else:
        description = random.choice(descriptions_per_image[image])

        while (algs.jaccard.similarity(description, start_description_per_image[image]) < 0.2):
            description = random.choice(descriptions_per_image[image])
        final_description_per_image[image] = description

    for context in contexts_per_image[image]:
        question_study_json['images'].append({
            'filename': image,
            'description': final_description_per_image[image],
            'category': context
        })

for i in pilot_exp['images']:
    if (i['filename'] in count_image_descriptions and count_image_descriptions[i['filename']] >= 3):
        print("Image ", i['filename'])
    else:
        images_left.append(i['filename'])
        new_pilot_exp['images'].append(i)

# TODO: Run it just once more, the same way!! :) 
images_left = list(set(images_left))
print("Images left ", images_left)
print("Number of images left ", len(images_left))

print("Descriptions per image ", descriptions_per_image)

# If the image was seen 3 times, then take it out from pilot_exp.json
# And then push pilot_exp.json!!!
json_object = json.dumps(new_pilot_exp, indent=4)
 
# Writing to sample.json
with open("new_pilot_exp.json", "w") as outfile:
    outfile.write(json_object)

json_object = json.dumps(question_study_json, indent=4)

# Writing to sample.json
with open("new_question_elicitation_study.json", "w") as outfile:
    outfile.write(json_object)

json_object = json.dumps(descriptions_per_image, indent=4)

# Writing to sample.json
with open("descriptions_per_image.json", "w") as outfile:
    outfile.write(json_object)