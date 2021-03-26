import requests
from json import dumps
from constants import grid_size

from flask import Flask, request

app = Flask(__name__)

history = []
tab = []
for i in range(grid_size):
    tab.append([0] * grid_size)

@app.route('/place', methods=['POST'])
def place(body = None):
    body = request.json
    tab[body['x']][body['y']] = body['color']
    history.append(body)
    return ''

@app.route('/full', methods=['GET'])
def full():
   return dumps(tab)
    
@app.route('/history', methods=['GET'])
def get_history():
   return dumps(history)

# Aller sur 127.0.0.1:5000
app.run(host='0.0.0.0')
