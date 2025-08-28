from flask import Flask
from connection.bd_connection import Conexao
import os

app = Flask(__name__)

# Crie a conexão com seus dados MySQL
criar = Conexao()

@app.route("/")
def index():

    try:
        resultado = criar.set_inserirusuario("welber", "@.com.br", "2332323", "2025-12-10")
        return f'usuario inserido com sucesso!${resultado}'
    
    except Exception as e:
        return f"Erro: {e}"
   

criar.fechar()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

