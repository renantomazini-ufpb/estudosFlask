from flask import Flask, render_template, request

app = Flask(__name__)

registros = []

@app.route("/")
def home():
    return render_template("layout.html")

@app.route('/lista', methods = ['GET','POST', 'UPDATE'])
def listar():
    #print(registros)
    if request.method == "POST":
        if request.form.get("tarefaNome") and request.form.get("tarefaDescricao") and request.form.get("tarefaPrioridade"):
            registros.append({'tarefaNome': request.form.get('tarefaNome'),"tarefaDescricao" : request.form.get('tarefaDescricao'),"tarefaPrioridade": request.form.get("tarefaPrioridade"), "status": True})
            #print(registros)

    if request.method == "GET":
        return render_template('todo.html', registros=registros)
    
    if request.method == "UPDATE":
        
        pass

    return render_template('todo.html', registros=registros)



#rotas dinâmicas
@app.route('/aplicativo/<nome_aplicativo>')
def detalhar_aplicativo(nome_aplicativo):
    return render_template("aplicativo.html", nome_aplicativo=nome_aplicativo)