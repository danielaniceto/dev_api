from crypt import methods
from distutils.log import debug
from multiprocessing import reduction
from urllib import response
from flask import Flask, jsonify, request
import flask
import json

app = Flask(__name__)

desenvolvedores = [
    {'id': '0',
    'nome':'Gustavo',
    'habilidades': ['Python', 'Flask']
    },
    {'id': '1',
    'nome':'Aniceto',
    'habilidades':['Python','Django']}
]
# essa parte do codigo, devolve um desenvolvedor por ID, também altera um desenvolvedor e deleta.
#@app.get('/dev/<int:id>/') # - se o metodo usado for somente GET, podemos fazer dessa forma, o mesmo serve para POST, PUT, DELETE e demais
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE']) # - a passagem da rota pode ser feito assim também, especificando o método que vais usar

def desenvolvedor(id):
    if request.method == 'GET':
        try: 
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe'
            response = {'status':'erro', 'mensagem':mensagem}
        
        except Exception:
            mensagem = 'Erro desconhecido, procure o adm da API'
            response = {'status': 'erro', 'mensagem':mensagem}

        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify([{'status':'sucesso', 'mensagem': 'Registro excluído com sucesso'}])

# Listar todos os desenvolvedores e permite registrar um novo desenvolvedor.

@app.route('/dev/', methods=['POST','GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    
    elif request.method == 'GET':
        return jsonify (desenvolvedores)

if __name__ == '__main__':
    app.run(debug = True)