# Importando SQLite
import sqlite3 as lite

#criando a conexao
conn = lite.connect("dados.db")

#criando a tabela
cur = conn.cursor()
cur.execute("CREATE TABLE formulario (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia_em DATE, estado TEXT, assunto TEXT)")




