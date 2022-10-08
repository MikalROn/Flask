from crypt import methods
from flask import Flask, render_template, request, redirect
from dataclasses import dataclass

@dataclass
class Jogo:
    nome: str
    categoria: str
    console: str

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Hack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista = [jogo1, jogo2, jogo3]


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

app.run(debug=True)

