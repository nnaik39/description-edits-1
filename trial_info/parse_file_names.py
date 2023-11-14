import json 
import os 
import textdistance 

string_a = 'Hello World!'
string_b = 'Hello Word!'

algs = textdistance.algorithms
algs.levenshtein.distance(string_a, string_b)
# Distance equals 1.0
algs.levenshtein.similarity(string_a, string_b)
# Similarity equals 11
algs.levenshtein.normalized_similarity(string_a, string_b)

# Jaccard similarity of 0.2 between the start description and the final description
print(algs.jaccard.similarity(string_a, string_b))
print(algs.jaccard.distance(string_a, string_b))
print(algs.jaccard.normalized_similarity(string_a, string_b))

f = open('pilot_exp.json')
 
# returns JSON object as
# a dictionary
pilot_exp = json.load(f)
 
# Iterating through the json
# list

# Open this here
f = open('description-editing-final-export.json')
study_info = json.load(f)

count_image_descriptions = {}
new_pilot_exp = {}
new_pilot_exp['images'] = []

descriptions_per_image = {}

for participant in study_info:
    for trial in study_info[participant]:
        if (trial['picture'] not in count_image_descriptions):
            count_image_descriptions[trial['picture']] = 0
        count_image_descriptions[trial['picture']] += 1
        if (trial['comments'] != ''):
            print(trial['comments'])
        if (trial['glb_comments'] != ''):
            print(trial['glb_comments'])
        if (trial['picture'] not in descriptions_per_image):
            descriptions_per_image[trial['picture']] = []
        descriptions_per_image[trial['picture']].append(trial['final_description'])

images_left = []
# See if the final descriptions are different here?

for i in pilot_exp['images']:
    if (i['filename'] in count_image_descriptions and count_image_descriptions[i['filename']] >= 3):
        print("Image ", i['filename'])
    else:
        images_left.append(i['filename'])
        new_pilot_exp['images'].append(i)

images_left = list(set(images_left))
print("Number of images left ", len(images_left))
print("Descriptions per image ", descriptions_per_image)

# If it's seen 3 times, then take it out from pilot_exp.json
# And then push pilot_exp.json!!!
json_object = json.dumps(new_pilot_exp, indent=4)
 
# Writing to sample.json
with open("new_pilot_exp.json", "w") as outfile:
    outfile.write(json_object)
