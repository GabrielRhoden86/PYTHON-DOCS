from Conexao import Conexao

class CRUD:
    def __init__(self, conexao):
        self.conexao = conexao

    def read(self):
        cursor = self.conexao.get_cursor()
        cursor.execute("SELECT * FROM queries")
        results = cursor.fetchall()
        for row in results:
            print(row)

    def create(self, nome, tags, query):
        cursor = self.conexao.get_cursor()
        insert_query = "INSERT INTO queries (nome, tags, query) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (nome, tags, query))
        self.conexao.commit()
        
    def update(self, nome, tags, query, id):
        cursor = self.conexao.get_cursor()
        update_query = "UPDATE queries SET nome = %s, tags = %s, query = %s WHERE id = %s"
        cursor.execute(update_query, (nome, tags, query, id))
        self.conexao.commit()

    def delete(self, id):
       cursor = self.conexao.get_cursor()
       delete_query = "DELETE FROM queries WHERE id = %s"
       cursor.execute(delete_query, (id,))
       self.conexao.commit()
       
conexao = Conexao()
crud = CRUD(conexao)

# Inserir um novo registro
# crud.create("nome_exemplo", "tags_exemplo", "query_exemplo")

# Ler registros
# crud.read()

# Atualizar um registro existente
# crud.update("novo_nome", "novas_tags", "nova_query", 24)

# Excluir um registro existente
# crud.delete(25)


# Fechar a conexão
conexao.close()
