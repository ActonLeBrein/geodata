import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = address
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('comments/comment')
    count = 0
    for result in results:
        count += int(result.find('count').text)
    print(count)