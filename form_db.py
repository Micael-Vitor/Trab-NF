#Emissor de nota fiscal
import sqlite3 as sql

con = sql.connect('form_db.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS users')

sql = '''CREATE TABLE ''users''(
    ''ID'' INTEGER PRIMARY KEY AUTOINCREMENT,
    ''NOME'' TEXT,
    ''CPF'' TEXT,
    ''ENDERECO'' INTEGER
    ''VPRODUTO'' FLOAT
    ''PESO'' FLOAT
    ''IDNOTA'' INTEGER 
    )'''

cur.execute(sql)
con.commit()
con.close()


