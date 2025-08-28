import mysql.connector
from mysql.connector import Error

class Conexao:

    def __init__(self, host="127.0.0.1", user="root", password="Yeshua77*w", database="doacoes"):
        try:
            self.conexao = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.conexao.cursor()
            print("Conexão MySQL estabelecida com sucesso!")
        except Error as e:
            print("Erro ao conectar ao MySQL:", e)


    def get_conectar(self):
        return self.conexao

    def get_cursor(self):
        return self.cursor

    def commit(self):
        if self.conexao:
            self.conexao.commit()

    def fechar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao and self.conexao.is_connected():
            self.conexao.close()
            print("Conexão MySQL fechada.")
