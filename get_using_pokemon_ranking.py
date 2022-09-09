import requests

response = requests.get('https://resource.pokemon-home.com/battledata/ranking/10311/2/1656642103/pokemon')


with open('using_pokemon_ranking.json', 'wb') as f:
    f.write(response.content)