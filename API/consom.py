import requests
from json import dumps

# # Ici on récupère un dictionnaire de valeurs
res = requests.get('http://127.0.0.1:5000/hello1').json()

# # Le corps d'une requête au format dict aussi
body = { 'value': res['name'] }

# # Headers HTTP pour indiquer le format au serveur
headers = { 'content-type': 'application/json' }

# # Ici on effectue un POST avec notre body en JSON
requests.post('http://127.0.0.1:5000/hello1',dumps(body),headers=headers)