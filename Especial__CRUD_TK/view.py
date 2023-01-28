# Importando SQLite
import sqlite3 as lite


####### CRUD #######
# C - Create (inserir/criar) 
# R - Read (ler/acessar/mostrar)
# U - Update (atualizar)
# D - Delete (deletar)


#criando a conexao
conn = lite.connect("dados.db")


# Inserir Informações
def inserir_info(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO formulario (nome, email, telefone, dia_em, estado, assunto) VALUES(?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)


# Acessar Informações
def mostrar_info():
    lista = []
    with conn:
        cur = conn.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        informacao = cur.fetchall()
        
        for i in informacao:
            lista.append(i)
            
    return lista
            

# Atualizar Informações
def atualizar_info(i):
    with conn:
        cur = conn.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, assunto=? WHERE id=?"
        cur.execute(query, i)


# Deletar/excluir Informações
def deleltar_info(i):
    with conn:
        cur = conn.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query, i)
