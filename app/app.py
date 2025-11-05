from flask import Flask, render_template, request
import random as rd

app = Flask(__name__)

usuarios = ['Renan', 'Andre', 'Bruna', 'Fernanda']

@app.route('/')
def main():
    num = rd.randrange(1,60)
    return render_template("index.html", N_sorte=num)

@app.route('/lista')
def listar():
    lista_jogos = ['Civilization VI', 'Cult of the lamb',"No I'm not human", 'Bem feito', "Telethugs", 'Sim City 4', 'Age of Empires 2', 'Need for Speed Hot Pursuit']
    return render_template("lista.html", jogos=lista_jogos)

@app.route('/sites')
def dic():
    links = {'Doc Python':'https://docs.python.org/3/', 'Flask': 'https://flask.palletsprojects.com/en/stable/', 'cheeats sheets':'https://cheatsheets.zip/flask'}
    return render_template('links_uteis.html', links=links)

@app.route('/lista_usuarios', methods = ["GET", "POST"])
def fusers():
    #usuarios = []
    if request.method == "POST":
        if request.form.get("nome"):
            usuarios.append(request.form.get("nome"))
    return render_template('usuarios_tab.html', usuarios = usuarios)


@app.route('/sobre')
def sobre():
    return render_template("sobre.html")