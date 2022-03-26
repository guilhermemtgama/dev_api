from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolverdores = [

    {'ID': '0',
     'nome': 'Guilherme Gama',
     'habilidades': ['Python, Flask']
     },
    {'ID': '1',
     'nome': 'Leticia Gama',
     'habilidades': ["Python", 'Django']}
]
# devolve um desenvolvedor pelo ID,também altera e deleta um desenvolvedor.
@app.route('/dev/<int:id>/', methods = ['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolverdores[id]
        except IndexError:
            mensagem = 'Desenvolverdor de ID {} não existe'.format(id)
            response = { 'status ': 'erro', 'mensagem ': mensagem }
        except Exception:
            mensagem = 'Erro desconhecido. Procure o adm da API'
            response = {'status': 'erro', 'mensagem': mensagem }
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolverdores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolverdores.pop(id)
        return jsonify({'status': 'Sucesso', 'mensagem':'Registro excluido'})


# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor

@app.route('/dev/', methods = ['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolverdores)
        dados['id'] = posicao
        desenvolverdores.append(dados)
        return jsonify(desenvolverdores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolverdores)




if __name__ == '__main__':
    app.run(debug=True)