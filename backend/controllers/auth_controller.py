from flask import request, render_template, redirect, url_for, make_response
from services.auth_service import autenticar_usuario, gerar_token

def home():
    return render_template("login.html")

def login():

    print("LOGIN CHAMADO")

    email = request.form.get("email")
    senha = request.form.get("senha")

    usuario = autenticar_usuario(email,senha)

    if not usuario:
        return render_template("login.html", erro="E-mail ou senha incorretos.")
    
    token = gerar_token(usuario["id"])

    response = make_response(redirect(url_for('auth.dashboard')))
    response.set_cookie("access_token", token, httponly=True)

    return response

def dashboard():
    return render_template("dashboard.html")

def logout():
    resp = make_response(redirect(url_for('auth.home')))
    resp.delete_cookie("access_token")
    return resp