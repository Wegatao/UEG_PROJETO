import mysql.connector
from mysql.connector import Error
       
# Classe que gerencia a conexão e operações com o banco de dados
class Conexao:
        def __init__(self, config):
         self.config = config # Configuração do banco de dados

        def conectar(self):
         try:
            conexao = mysql.connector.connect(**self.config)
            if conexao.is_connected():
                print("Conexão bem-sucedida com o banco de dados.")
                return conexao
         except Error as e:
                print(f"Erro ao conectar no MySQL: {e}")
                return None
    

       # Cria a tabela "cooperados" se ela não existir
        def set_inserirusuario(self, nome, email, senha, dataInscricao):
          conexao = self.conectar()
        
          if conexao:
            try:
              cursor = conexao.cursor()
              cursor.execute("""
                INSERT INTO Pendencias (nome, email, senha, dataInscricao)
                VALUES (%s, %s, %s, %s)
                """, (nome, email, senha, dataInscricao))
              
              conexao.commit()
              return {"sucesso": True, "mensagem": "Pendência cadastrada com sucesso"}
            
            except Error as e:
              print(f"Erro ao cadastrar pendência: {e}")
              return {"sucesso": False, "mensagem": f"Erro: {e}"}
            finally:
              conexao.close()
            
       
       




