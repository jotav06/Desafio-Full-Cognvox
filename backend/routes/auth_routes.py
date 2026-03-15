from flask import Blueprint, request, render_template, redirect, url_for, make_response
import bcrypt
import jwt
import datetime
from database import get_connection

# Criamos o Blueprint
auth_bp = Blueprint('auth', __name__)

SECRET_KEY = "super_secret_key"

@auth_bp.route("/")
def home():
    return render_template("login.html")

@auth_bp.route("/login", methods=["POST"])
def login():
    # Agora pegamos os dados do FORMULÁRIO (HTML), não do JSON
    email = request.form.get("email")
    senha = request.form.get("senha")

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE email=%s", (email,))
    usuario = cursor.fetchone()

    # Validação de usuário e senha
    if not usuario or not bcrypt.checkpw(senha.encode(), usuario["senha_hash"].encode()):
        # Se falhar, recarrega a página de login passando uma mensagem de erro
        return render_template("login.html", erro="E-mail ou senha incorretos.")

    # Geração do Token JWT
    payload = {
        "user_id": usuario["id"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    # Criamos a resposta de redirecionamento para o dashboard
    response = make_response(redirect(url_for('auth.dashboard')))
    
    # Salvamos o token no Cookie do navegador
    # httponly=True impede que scripts maliciosos acessem o token
    response.set_cookie('access_token', token, httponly=True)
    
    return response

@auth_bp.route("/dashboard")
def dashboard():
    # Verificamos o token diretamente nos cookies do navegador
    token = request.cookies.get('access_token')
    
    if not token:
        return redirect(url_for('auth.home'))

    try:
        # Validamos o token
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return render_template("dashboard.html")
    
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        # Se o token expirou ou é inválido, limpamos o cookie e voltamos ao login
        resp = make_response(redirect(url_for('auth.home')))
        resp.delete_cookie('access_token')
        return resp

@auth_bp.route("/logout")
def logout():
    # Rota simples para sair
    resp = make_response(redirect(url_for('auth.home')))
    resp.delete_cookie('access_token')
    return resp
