import mysql.connector
from mysql.connector import Error

class Conexao:

    def __init__(self, host="br268.hosgator.com.br", user="welber77_welber", password="1Ddeprs1#", database="welber77_root01"):
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




