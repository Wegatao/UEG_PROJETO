from flask import Flask
from connection.bd_connection import Conexao

app = Flask(__name__)

# Crie a conexão com seus dados MySQL
criar = Conexao()

@app.route("/")
def index():

    try:
        resultado = criar.set_inserirusuario("welber", "@.com.br", "2332323", "2025-12-10")
        return ({'usuario inserido com sucesso!', resultado})
    
    except Exception as e:
        return f"Erro: {e}"
   

criar.fechar()
if __name__ == "__main__":
    app.run(debug=True)
