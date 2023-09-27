import mysql.connector

class Conexao:
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="new_site"
        )
        self.cursor = self.con.cursor()

    def get_cursor(self):
        return self.cursor

    def commit(self):
        self.con.commit()

    def close(self):
        self.cursor.close()
        self.con.close()