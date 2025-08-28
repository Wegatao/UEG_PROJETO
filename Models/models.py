from connection.bd_connection import Conexao



class Cricao_tabela:
    
    def __init__(self):
        self.db = Conexao()
        self.cursor = self.db.get_cursor()

    def set_criarUsuario(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    email VARCHAR(255),
                    senha VARCHAR(255) NOT NULL,
                    dataInscricao DATE NOT NULL
                )""")
            self.db.commit()
        finally:
            self.cursor.close()

    def set_inserirusuario(self, nome, email, senha, dataIncricao):
        try:
            self.cursor.execute("insert into usuarios(nome, email, senha, dataIncricao) Values(%s,%s,%s,%s)",
                       (nome, email, senha, dataIncricao))
            self.db.commit()
        finally:
            self.cursor.close()



       
