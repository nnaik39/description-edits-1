import json

f = open('all_images_with_descriptions.json')
data = json.load(f)

contexts_assigned_to_image = {}

# Write out some numbers here, and include them in the paper!!

# Each image is assigned two contexts!!
# For each image here

context_pairs_count = {}

for datapoint in data['images']:
    if (datapoint['filename'] not in contexts_assigned_to_image):
        contexts_assigned_to_image[datapoint['filename']] = []
    
    contexts_assigned_to_image[datapoint['filename']].append(datapoint['category'])

for image in contexts_assigned_to_image:
    # Make the contexts assigned 

    contexts_assigned_to_image[image].sort()
    
    contexts = tuple((contexts_assigned_to_image[image]))

    if (contexts not in context_pairs_count):
        context_pairs_count[contexts] = 0
    context_pairs_count[contexts] += 1

print("Context pairs count ", context_pairs_count)