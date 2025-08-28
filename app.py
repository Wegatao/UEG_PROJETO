from flask import Flask
from Models.models import Cricao_tabela

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
    app.run(debug=True)
