from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import json
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1414CAca@localhost/flaskAPIv1'

db = SQLAlchemy(app)


# tabela de produtos
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    preco = db.Column(db.Float)

    def to_json(self):
        return {"id": self.id, "nome": self.nome, "preco": self.preco}


# tabela de maquinas
class Maquina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(50))
    status = db.Column(db.String(20))

    def to_json(self):
        return {"id": self.id, "modelo": self.modelo, "status": self.status}


# tabela de talhoes
class Talhao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tamanho = db.Column(db.Float)
    geoloc = db.Column(db.String(50))
    status = db.Column(db.String(20))

    def to_json(self):
        return {"id": self.id, "tamanho": self.tamanho, "geoloc": self.geoloc, "status": self.status}


# tabela de safras
class Safra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ano = db.Column(db.Integer)
    cultivar = db.Column(db.String(20))
    status = db.Column(db.String(20))

    def to_json(self):
        return {"id": self.id, "ano": self.ano, "cultivar": self.cultivar, "status": self.status}


# seleciona todos os produtos
@app.route('/produtos', methods=['GET'])
def seleciona_produtos():
    produtos_objetos = Produto.query.all()
    produtos_json = [produto.to_json() for produto in produtos_objetos]

    return gera_response(200, "produtos", produtos_json)


# seleciona todas as maquinas
@app.route('/maquinas', methods=['GET'])
def seleciona_maquinas():
    maquinas_objetos = Maquina.query.all()
    maquinas_json = [maquina.to_json() for maquina in maquinas_objetos]

    return gera_response(200, "maquinas", maquinas_json)


# seleciona todos os talhoes
@app.route('/talhoes', methods=['GET'])
def seleciona_talhoes():
    talhoes_objetos = Talhao.query.all()
    talhoes_json = [talhao.to_json() for talhao in talhoes_objetos]

    return gera_response(200, "talhoes", talhoes_json)


# seleciona todas as safras
@app.route('/safras', methods=['GET'])
def seleciona_safras():
    safras_objetos = Safra.query.all()
    safras_json = [safra.to_json() for safra in safras_objetos]

    return gera_response(200, "safras", safras_json)


# selecionar produto individualmente
@app.route('/produto/<id>', methods=["GET"])
def seleciona_produto(id):
    produto_objeto = Produto.query.filter_by(id=id).first()
    produto_json = produto_objeto.to_json()

    return gera_response(200, 'produto', produto_json)


# selecionar maquina individualmente
@app.route('/maquina/<id>', methods=["GET"])
def seleciona_maquina(id):
    maquina_objeto = Maquina.query.filter_by(id=id).first()
    maquina_json = maquina_objeto.to_json()

    return gera_response(200, 'maquina', maquina_json)


# selecionar talhao individualmente
@app.route('/talhao/<id>', methods=["GET"])
def seleciona_talhao(id):
    talhao_objeto = Talhao.query.filter_by(id=id).first()
    talhao_json = talhao_objeto.to_json()

    return gera_response(200, 'talhao', talhao_json)


# selecionar safra individualmente
@app.route('/safra/<id>', methods=["GET"])
def seleciona_safra(id):
    safra_objeto = Safra.query.filter_by(id=id).first()
    safra_json = safra_objeto.to_json()

    return gera_response(200, 'safra', safra_json)


# cadastrar produto
@app.route("/produto", methods=["POST"])
def cria_produto():
    body = request.get_json()

    # validar os parametros com try e exeption
    try:
        produto = Produto(nome=body["nome"], preco=body["preco"])
        db.session.add(produto)
        db.session.commit()
        return gera_response(201, "produto", produto.to_json(), "Produto criado com sucesso")

    except Exception as e:
        print(e)
        return gera_response(400, "produto", {}, "Erro ao cadastrar")


# cadastrar maquina
@app.route("/maquina", methods=["POST"])
def cria_maquina():
    body = request.get_json()

    # validar os parametros com try e exeption
    try:
        maquina = Maquina(modelo=body["modelo"], status=body["status"])
        db.session.add(maquina)
        db.session.commit()
        return gera_response(201, "maquina", maquina.to_json(), "Maquina criada com sucesso")

    except Exception as e:
        print(e)
        return gera_response(400, "Maquina", {}, "Erro ao cadastrar")


# cadastrar talhao
@app.route("/talhao", methods=["POST"])
def cria_talhao():
    body = request.get_json()

    # validar os parametros com try e exeption
    try:
        talhao = Talhao(tamanho=body["tamanho"], geoloc=body["geoloc"], status=body["status"])
        db.session.add(talhao)
        db.session.commit()
        return gera_response(201, "talhao", talhao.to_json(), "Talhao criado com sucesso")

    except Exception as e:
        print(e)
        return gera_response(400, "talhao", {}, "Erro ao cadastrar")


# cadastrar safra
@app.route("/safra", methods=["POST"])
def cria_safra():
    body = request.get_json()

    # validar os parametros com try e exeption
    try:
        safra = Safra(ano=body["ano"], cultivar=body["cultivar"], status=body["status"])
        db.session.add(safra)
        db.session.commit()
        return gera_response(201, "safra", safra.to_json(), "Safra criada com sucesso")

    except Exception as e:
        print(e)
        return gera_response(400, "talhao", {}, "Erro ao cadastrar")


# deletar produto
@app.route('/produto/<id>', methods=["DELETE"])
def deleta_produto(id):
    produto_objeto = Produto.query.filter_by(id=id).first()

    try:
        db.session.delete(produto_objeto)
        db.session.commit()
        return gera_response(200, "produto", produto_objeto.to_json(), "Produto deletado com sucesso")

    except Exception as e:
        print("Erro", e)
        return gera_response(400, "produto", {}, "Erro ao deletar")


# deletar maquina
@app.route('/maquina/<id>', methods=["DELETE"])
def deleta_maquina(id):
    maquina_objeto = Maquina.query.filter_by(id=id).first()

    try:
        db.session.delete(maquina_objeto)
        db.session.commit()
        return gera_response(200, "maquina", maquina_objeto.to_json(), "Maquina deletada com sucesso")

    except Exception as e:
        print("Erro", e)
        return gera_response(400, "maquina", {}, "Erro ao deletar")


# deletar talhao
@app.route('/talhao/<id>', methods=["DELETE"])
def deleta_talhao(id):
    talhao_objeto = Talhao.query.filter_by(id=id).first()

    try:
        db.session.delete(talhao_objeto)
        db.session.commit()
        return gera_response(200, "talhao", talhao_objeto.to_json(), "Talhao deletado com sucesso")

    except Exception as e:
        print("Erro", e)
        return gera_response(400, "talhao", {}, "Erro ao deletar")


# deletar safra
@app.route('/safra/<id>', methods=["DELETE"])
def deleta_safra(id):
    safra_objeto = Safra.query.filter_by(id=id).first()

    try:
        db.session.delete(safra_objeto)
        db.session.commit()
        return gera_response(200, "safra", safra_objeto.to_json(), "Safra deletada com sucesso")

    except Exception as e:
        print("Erro", e)
        return gera_response(400, "safra", {}, "Erro ao deletar")


# gerar as respostas das requisições
def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {nome_do_conteudo: conteudo}
    # se tiver uma mensagem, coloca ela no body
    if mensagem:
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")


app.run()
