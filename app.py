from flask import Flask
from flask import Flask, jsonify, request
from connection.bd_connection import Conexao
from connection.confing import CONFING
import os
app = Flask(__name__)
conexao = Conexao(CONFING)



@app.route("/")
def index():
    return jsonify('esta tudo certo')

@app.route("/InserirNovoUsuario", methods=["POST"])
def cadastrarPessoa():
    dados = request.json
    resultado = conexao.set_inserirusuario(
        dados['nome'], dados['email'], dados['senha'], dados['dataInscricao']
    )
    sucesso = resultado.get("mensagem") == "ok"
    return jsonify({"sucesso": sucesso, "resultado": resultado}), 200 if sucesso else 400



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)


