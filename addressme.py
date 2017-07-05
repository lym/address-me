import argparse
import json

import requests


class AddressMe:
    def __init__(self):
        mapcode_api_url = 'https://api.mapcode.com/'
        mapcode_codes_resource_path = 'mapcode/codes/'
        parser = argparse.ArgumentParser(
            description='Simple commandline utility that returns a map code'
        )

        parser.add_argument(
            '--lat', dest='lat', type=float, help='The latitude.'
        )
        parser.add_argument(
            '--lon', dest='lon', type=float, help='The longitude..'
        )
        arguments = parser.parse_args()

        self.mapcode_codes_resource_url  = mapcode_api_url + mapcode_codes_resource_path  # NOQA
        self.latitude  = arguments.lat
        self.longitude = arguments.lon

    def get_mapcode(self, lat, lon):
        print(
            'latitude is: {}\nlongitude is: {}'.format(
                self.latitude, self.longitude
            )
        )

        req = requests.get(
            '{}{},{}'.format(
                self.mapcode_codes_resource_url, self.latitude, self.longitude)
        )

        # We need to decode the bytestring that is returned by the requests
        # library
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

        print(
            "Status Code: {}\n\nCodes: {}".format(
                req.status_code, returned_codes)
        )


if __name__ == '__main__':
    addresser = AddressMe()
    addresser.get_mapcode(addresser.latitude, addresser.longitude)
