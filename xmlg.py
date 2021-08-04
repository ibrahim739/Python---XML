import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
from bs4 import BeautifulSoup

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'https://sparkaligners.com/contact-us/find-provider/'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(address, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())

    counter = 0
    count = 0
    sum = 0
    tree = ET.fromstring(data)
    # Look for any specific data that you want by entering the anchor tag
    counts = tree.findall('.//count')
    for counter in counts:
        sum = sum + int(counter.text)
        count = count + 1
    print(sum)
    print(count)
