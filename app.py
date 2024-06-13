from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
@app.route("/index")

def index():
     con = sql.connect('form_db.db')
     con.row_factory=sql.Row
     cur=con.cursor()
     cur.execute('select " from users')
     data=cur.fetchall()
     return render_template('index.html', datas=data)


@app.route('/add_user', methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        nome=request.form['nome']
        cpf=request.form['cpf']
        endereco=request.form['endereco']
        VProduto=request.form['VProduto']
        peso=request.fomr['peso']
        IdNota=request.form['IdNota']
        con=sql.connect('form_db.db')
        cur=con.cursor()
        cur.execute('insert into users(NOME, CPF, ENDERECO, VPRODUTO, PESO, IDNOTA,) values (?, ?, ?, ?, ?, ?)', (nome, cpf, endereco, VProduto, peso, IdNota))
        con.commit()
        flash('Dados cadastrados', 'sucesso')
        return redirect(url_for('index'))
    return render_template('add_user.html')


@app.route('/edit_user/<string:id>', methods=['POST', 'GET'])
def edit_user(id):
    if request.method=='POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        endereco = request.form['endereco']
        VProduto = request.form['float']
        peso = request.fomr['float']
        IdNota = request.form['IdNota']
        con=sql.connect('form_db.db')
        cur=con.cursor()
        cur.execute('update users set NOME=?, CPF=?, ENDERECO=?, VPRODUTO=?, PESO=?, IDNOTA=?, where ID=?', (nome, cpf, endereco, VProduto, peso, IdNota))
        con.commit()
        flash('Dados atualizados', 'sucesso')
        return redirect(url_for('index'))
    con=sql.connect('form_db.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute('select * from users where ID=?', (id,))
    data=cur.fetchone()
    return render_template('edit_user.html', datas=data)

@app.route('/delete_user<string:id>', methods=['GET'])
def delete_user(id):
        con=sql.connect('form_db.db')
        cur=con.cursor()
        cur.execute('delete from users where ID=?', (id,))
        con.commit()
        flash('Dados deletados')
        return redirect(url_for('index'))

if __name__=='__main__':
    app.secret.key='admin123'
    app.run(debug=True)




