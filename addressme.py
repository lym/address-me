import argparse
import json

import requests

parser = argparse.ArgumentParser(
    description='Simple commandline utility that returns a map code'
)

parser.add_argument('--lat', dest='lat', type=float, help='The latitude.')
parser.add_argument('--lon', dest='lon', type=float, help='The longitude..')
arguments = parser.parse_args()

latitude  = arguments.lat
longitude = arguments.lon

print(
    'latitude is: {}\nlongitude is: {}'.format(latitude, longitude)
)

mapcode_api_url = 'https://api.mapcode.com/'
mapcode_codes_resource_path = 'mapcode/codes/'
mapcode_codes_resource_url  = mapcode_api_url + mapcode_codes_resource_path

# test_lat = # 0.341510
# test_lon = # 32.593860

req = requests.get(
    '{}{},{}'.format(mapcode_codes_resource_url, latitude, longitude)
)

# We need to decode the bytestring that is returned by the requests library
response_content = json.loads(bytes.decode(req.content))
mapcodes = response_content.get('mapcodes')

returned_codes = []
territories    = []
for el in mapcodes:
    for key, value in el.items():
        if key == 'mapcode':
            returned_codes.append(value)
        else:
            territories.append(value)

print("Status Code: {}\n\nCodes: {}".format(req.status_code, returned_codes))
