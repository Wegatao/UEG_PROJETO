from flask import Flask
from Models.models import Cricao_tabela
import os

app = Flask(__name__)

# Crie a conexão com seus dados MySQL
criar = Cricao_tabela()

@app.route("/")
def index():

    try:
        criar.set_criarUsuario()
        criar.set_inserirusuario("welber", "@.com.br", "2332323", "2025-12-10")
        criar.get_fechar()
        return 'usuario inserido com sucesso!'
    
    except Exception as e:
        return f"Erro: {e}"
        
if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 5000))  # Pega a porta da Render ou usa 5000
    app.run(host="0.0.0.0", port=porta, debug=True)

