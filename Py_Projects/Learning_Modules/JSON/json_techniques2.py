"""Learn more about the python json module"""

import json


# How to load a json file
with open('states.json') as f:
    data = json.load(f)
# Create a simple loop to delete area_code values from the initial data object
for state in data['states']:
    del state['area_codes']

# Create a new json file with the updated data use 'w' to specify write
with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)
