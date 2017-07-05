# AddressMe
addressme is a simple commandline utility that returns a map code
corresponding to the supplied latitude and logitude arguments.

A mapcode is simple string representing a location.

Sample latitude, longitude pair:
lat:  0.341510
lon: 32.593860

# Usage

## Install requirements

    $ pip install pip-tools
    $ pip-sync requirements.txt

## Excute CLI

    $ ./addressme --lat [latitude] --lon [longitude]

e.g.;

    $ addressme.py --lat 0.341510 --lon 32.593860

### Sample response
latitude is: 0.34151
longitude is: 32.59386
Status Code: 200

Codes: ['N7.GS', 'JC.NHT', 'CYD.Z8H', 'KP43.FLP', 'HL9P6.NF45']
