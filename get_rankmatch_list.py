import requests

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'countrycode': '304',
    'authorization': 'Bearer',
    'langcode': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36',
    # Already added when you pass json=
    # 'content-type': 'application/json',
}

json_data = {
    'soft': 'Sw',
}

response = requests.post('https://api.battle.pokemon-home.com/cbd/competition/rankmatch/list', headers=headers, json=json_data)

with open('season.json', 'wb') as f:
    f.write(response.content)