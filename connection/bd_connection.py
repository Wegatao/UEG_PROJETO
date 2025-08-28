import mysql.connector
from mysql.connector import Error

class Conexao:

    def __init__(self, host="br268.hostgator.com.br", user="welber77_welber", password="Yeshua77*w", database="welber77_welberBancoDB"):
        try:
            self.conexao = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
        except Error as e:
            print("Erro ao conectar ao MySQL:", e)

    def set_criarUsuario(self):
        cursor = self.conexao.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    email VARCHAR(255),
                    senha VARCHAR(255) NOT NULL,
                    dataInscricao DATE NOT NULL
                )
            """)
            self.conexao.commit()
        finally:
            cursor.close()  # só fecha o cursor, mantém a conexão aberta

    def set_inserirusuario(self, nome, email, senha, dataInscricao):
        cursor = self.conexao.cursor()
        try:
            cursor.execute(
                "INSERT INTO usuarios(nome, email, senha, dataInscricao) VALUES (%s,%s,%s,%s)",
                (nome, email, senha, dataInscricao)
            )
            self.conexao.commit()
            return {'mensagem': 'ok'}
        except Error as e:
            return e
        finally:
            cursor.close()  # só fecha o cursor

    def fechar(self):
        if self.conexao and self.conexao.is_connected():
            self.conexao.close()
            print("Conexão MySQL fechada.")
