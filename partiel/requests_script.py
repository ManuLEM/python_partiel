import requests

banks = requests.get('http://localhost:5000/banks')

json_banks = banks_resp.json()

for bank in json_banks['_items']:
    print('Country: ', bank['countryname'])
    print('Link: ', bank['url'])