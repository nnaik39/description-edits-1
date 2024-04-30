import json

f = open('old_context_assignments.json')
data = json.load(f)

pilot_exp = {}
pilot_exp['images'] = []

# Compile a description editing study
# Make sure each filename starts with 'images/' and ends with '.jpeg'

for file in data:
    # Check if it begins with images/ AND ends with .jpeg
    # Check if there are any special characters in the filename (non alphanumeric or _)
    if (not(file['filename'].startswith('images/') or file['filename'].endswith('.jpeg'))):
        print("Incorrectly formatted image: ", file)

    entry = {
        'filename': file['filename'],
        'description': file['description']
    }

    if (entry not in pilot_exp['images']):
        pilot_exp['images'].append({
            'filename': file['filename'],
            'description': file['description']
        })

with open('scaledup_pilot_exp.json', 'w') as f:
    f.write(json.dumps(pilot_exp))