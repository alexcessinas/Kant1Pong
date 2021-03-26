import requests
from json import dumps

from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/hello/',methods=['POST','GET'])
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)


@app.route('/hello1/', methods=['POST','GET'])
def hello1():
    if request.method == 'POST':
        body = request.json
        print(body['value'])
        return body['value']
    elif request.method == 'GET':
        print('GET request')
        return {'name': 'Alex'}
   

# Aller sur 127.0.0.1:5000
app.run(host='0.0.0.0')

# # Ici on récupère un dictionnaire de valeurs
res = requests.get('http://127.0.0.1:5000/user').json()

# # Le corps d'une requête au format dict aussi
body = { 'value': res['name'] }

# # Headers HTTP pour indiquer le format au serveur
headers = { 'content-type': 'application/json' }

# # Ici on effectue un POST avec notre body en JSON
requests.post('http://127.0.0.1:5000/hello',dumps(body),headers=headers)