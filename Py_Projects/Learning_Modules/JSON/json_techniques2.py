"""Learn more about the python json module"""

import json


# We first open the json file as variable f and set data = json.load(f)
# We simply load the initial json file
with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    del state['area_codes']

# Just as before we need to open a new file called new_states.json
# You must use the 'w' to write the file out and you have created a
# new json file voila!
with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)
