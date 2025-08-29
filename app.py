from flask import Flask
from flask import Flask, jsonify
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
    dados = ('welber','111','wewew',1010)
    resultado = conexao.set_inserirusuario(dados)
    return jsonify(resultado), 200 if resultado.get("sucesso") else 400


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
