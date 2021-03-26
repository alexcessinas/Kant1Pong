import requests
from json import dumps

from flask import Flask, request

app = Flask(__name__)

@app.route('/place', methods=['POST'])
def place():
    return
    
@app.route('/full', methods=['GET'])
def full():
   return

# Aller sur 127.0.0.1:5000
app.run(host='0.0.0.0')
