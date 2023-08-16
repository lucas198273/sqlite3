from flask import Flask, jsonify, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Configurações do Flask
app.config['SECRET_KEY'] = "palavra_secreta"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização do SQLAlchemy e Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Modelo do Produto
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'preco': self.preco
        }

# Rotas da API
@app.route('/api/produtos', methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    return jsonify([produto.serialize() for produto in produtos])

@app.route('/api/produtos', methods=['POST'])
def criar_produto():
    dados = request.json
    novo_produto = Produto(nome=dados['nome'], preco=dados['preco'])
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify({'mensagem': 'Produto criado com sucesso!'})

# Resto das rotas e lógica do seu aplicativo (como autenticação, páginas HTML, etc.)

if __name__ == '__main__':
    app.run(debug=True)
