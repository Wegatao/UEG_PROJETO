from connection.bd_connection import Conexao



class Cricao_tabela:
    
    def __init__(self):
        self.db = Conexao()
        

    def set_criarUsuario(self):
        cursor = self.db.get_cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    email VARCHAR(255),
                    senha VARCHAR(255) NOT NULL,
                    dataInscricao DATE NOT NULL
                )""")
            self.db.commit()
        finally:
            cursor.close()

    def set_inserirusuario(self, nome, email, senha, dataIncricao):
        cursor = self.db.get_cursor()
        try:
            cursor.execute("insert into usuarios(nome, email, senha, dataIncricao) Values(%s,%s,%s,%s)",
                       (nome, email, senha, dataIncricao))
            self.db.commit()
        finally:
            cursor.close()

    def get_fechar(self):
        return self.db.fechar()
       

