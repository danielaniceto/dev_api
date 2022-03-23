from crypt import methods
from distutils.log import debug
from doctest import FAIL_FAST
from unicodedata import name
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.get('/<int:id>')
def pessoa(id):
    return jsonify ({'id':id, 'nome':'Daniel','profissao':'desenvolvedor'})

@app.get('/soma/<int:valor1>/<int:valor2>/')
def soma0(valor1, valor2):
   return jsonify({'soma': valor1 + valor2})

@app.post('/soma1')
def soma1():
    dado = json.loads(request.data)
    total = sum(dado['valores']) # depois do curso alterar essa variavel para "dados"
    return jsonify({'soma': total})

@app.route('/soma2', methods=['POST', 'GET'])
def soma2():
    if request.method == 'POST':
        dado = json.loads(request.data)
        total = sum(dado['valores'])

    elif request.method == 'GET':
        total = 10 + 10
    return jsonify({'soma': total})

if __name__ == '__main__':
    app.run(debug = False)