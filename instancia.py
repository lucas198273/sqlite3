from flask import Flask, jsonify, request

app = Flask(__name__)

clientes = clientes = [
    {
        'id': 1,
        'nome': 'Joao Magalhaes',
        'idade': 45,
        'email': 'jmisdiaodjiojido'
    },
    {
        'id': 2,
        'nome': 'Maria Silva',
        'idade': 32,
        'email': 'mariasilva@example.com'
    },
    {
        'id': 3,
        'nome': 'Carlos Souza',
        'idade': 28,
        'email': 'carlossouza@example.com'
    },
    {
        'id': 4,
        'nome': 'Joao Pedro',
        'idade': 45,
        'email': 'jmisdiaodjiojido'
    },
    {
        'id': 5,
        'nome': 'Maria Silva',
        'idade': 32,
        'email': 'mariasilva@example.com'
    },
    {
        'id': 6,
        'nome': 'Carlos Andrade',
        'idade': 28,
        'email': 'carlossouza@example.com'
    },
    {
        'id': 7,
        'nome': 'Marina',
        'idade': 4,
        'email': 'jmisdiaodjiojido'
    }
]

@app.route('/obter_cliente', methods=['GET'])
def obter_clientes():
    return jsonify(clientes)

@app.route('/obter_cliente/<int:id>', methods=['GET'])
def obter_por_id(id):
    for cliente in clientes:
        if cliente.get('id') == id:
            return jsonify(cliente)
@app.route('/obter_cliente/<int:id>',methods=['PUT'])
def editar_cliente(id):
    cliente_alterado = request.get_json() #lé dado passado pelo cliente
    for indice,cliente in enumerate(clientes):
        if cliente.get('id') == id: 
            clientes[indice].update(cliente_alterado)
            return jsonify(clientes[indice])
        
@app.route('/obter_cliente', methods=['POST'])
def incluir_cliente():
    novo_cliente = request.get_json() 
    clientes.append(novo_cliente)

    return jsonify(clientes) # so é possivel retornar dados em formato Json   

@app.route('/obter_cliente/<int:id>',methods=['DELETE'])
def deletar_cliente(id):
    for indice,cliente in enumerate(clientes):
        if cliente.get('id') == id:
            del clientes[indice]
    
    return jsonify(clientes)


if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)