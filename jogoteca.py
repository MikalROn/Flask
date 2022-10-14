from flask import Flask, render_template, request, redirect, session, flash, url_for


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Hack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = 'Miguel'


@app.route(url_for('index'))
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route(url_for('novo'))
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    return render_template('novo.html', titulo='Novo Jogo')


@app.route(url_for('criar'), methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')


@app.route(url_for('login'))
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route(url_for('autenticar'), methods=['POST', ])
def autenticar():
    if 'key' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(f'{session["usuario_logado"]} logado com sucesso!')
        proxima_pagnia = request.form['proxima']
        return redirect(f'/{proxima_pagnia}')
    else:
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')


app.run(debug=True)
