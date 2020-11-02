"""Learning Techniques with json module"""
import json


people_string = '''
{
    "people": [
    {
        "name": "John Smith",
        "phone": "458-935-5521",
        "emails": ["johnsmith1@yahoo.com", "johnsmithoneder@hotmail.com"],
        "has_license": false
    },
    {
        "name": "Jane Doe",
        "phone": "356-665-8971",
        "emails": ["jd124@aol.com","janedoe124@yahoo.com","janeydoey@hotmail.com"],
        "has_license": true
    }
  ]
}
'''

# Use json.loads to specify string to json object
data = json.loads(people_string)

# Basic loop to query certain data within the data object
for person in data['people']:
    if person['name'] == 'John Smith':
        del person['phone']
    elif person['name'] == 'Jane Doe':
        del person['emails']
        
# Use json.dumps to dump the new json object to a string
new_str = json.dumps(data, indent=2, sort_keys=True)

print(new_str)
