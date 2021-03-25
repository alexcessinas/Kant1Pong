import requests
from json import dumps

from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')

def hello(name=None):
    return render_template('index.jinja', name=name)

app.run(host='0.0.0.0')

# # Ici on récupère un dictionnaire de valeurs
# res = requests.get('http://api.com/user').json()

# # Le corps d'une requête au format dict aussi
# body = { 'value': res['name'] }

# # Headers HTTP pour indiquer le format au serveur
# headers = { 'content-type': 'application/json' }

# # Ici on effectue un POST avec notre body en JSON
# requests.post('http://api.com/hello',dumps(body),headers=headers)