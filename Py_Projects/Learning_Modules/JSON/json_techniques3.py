import requests
import json

# Read allows you to specify the size of the file as an option arg default -1 for entire file.
api_url = '**************'
payload = {'token': '*******'}
response = requests.get(api_url, headers=payload)

data = response.json()


# print(json.dumps(data,indent=2))
# check the meta data, use len to count the number of specific items in the json array
# print(len(data['results'))

# Initialize the results object outside of the loop and then append the new dictionary stations to the list of results.
results = []
for station in data['results']:
    stations = {}
    stations['name']= station['name']
    stations['latitude'] = station['latitude']
    stations['longitude'] = station['longitude']
    results.append(stations)

# Write the results to a json file
with open('station_nll.json', 'w') as f:
    json.dump(results, f, indent=2)
