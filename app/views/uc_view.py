from app import app
from flask import render_template
@app.route("/listuc")
def listar_uc():
    return render_template("uncompetencias/uc_template.html")

@app.route("/adduc")
def adicionar_uc():
    return "Adicionar unidade de competência"

@app.route("/deluc")
def excluir_uc():
    return "Excluir unidade de competência"

@app.route("/upuc")
def atualizar_uc():
    return "Atualizar unidade de competência"


@app.route("/meetuc",defaults={'nome':None},methods={'PUT'})
@app.route("/meetuc/<string:nome>")
def encontrar_uc(nome):
    if nome:
        return render_template("ucs/uc_temp.html",nome_uc=nome)
    else:
        return f"Navegue pelas UCs de forma personalizada"

@app.route("/numberuc/<int:numero>")
def number_uc(numero):
    match(numero):
        case 11: return f"UC {numero} -Lógica de Programação"
        case 12: return f"UC {numero} -Informática Básica"
        case _:return f" Dados inexistente"


@app.route("/login")
def login_ps():
    return "alô rota!"