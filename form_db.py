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



def opcoes():
    print('Criar NF: 1 \nEditar: 2 \nExcluir: 3 \nListar: 4')

opcoes()

OpcaoEscolhida = int(input('Digite a Opção Que gostaria: '))

match OpcaoEscolhida:
    #Criar NF
    case 1:
        print(f'Escolheu criar NF')
    #Editar NF
    case 2:
        print('Escolheu a opção editar')
    #Excluir NF
    case 3:
        print('Escolheu a opção excluir')
    #Listar todas NF
    case 4:
        print('Escolheu a opção listar')
    case _:
        print('Opção invalida')
