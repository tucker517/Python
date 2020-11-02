import requests
import json

# Read allows you to specify the size of the file as an option arg default -1 for entire file.
api_url = '**************'
payload = {'token': '*******'}
response = requests.get(api_url, headers=payload)

data = response.json()


# print(json.dumps(data,indent=2))
# check the meta data, use len to count the number of specific items in the json array
# print(len(data['list']['resources']))

# Here we store all of the json as a dictionary so that we may individually access data by using
# # [] on the usd_rates object which contains the name and price of the
stations = dict()

for station in data['results']:
    name = station['name']
    latitude = station['latitude']
    longitude = station['longitude']
    print(name, latitude, longitude)

with open('station_list.json', 'w') as f:
    json.dump(response, f, indent=2)
