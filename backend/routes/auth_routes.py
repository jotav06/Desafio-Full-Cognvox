from flask import Blueprint, request, render_template, redirect, url_for, make_response
import bcrypt
import jwt
import datetime
from database import get_connection


auth_bp = Blueprint('auth', __name__)

SECRET_KEY = "super_secret_key"

@auth_bp.route("/")
def home():
    return render_template("login.html")

@auth_bp.route("/login", methods=["POST"])
def login():
  
    email = request.form.get("email")
    senha = request.form.get("senha")

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE email=%s", (email,))
    usuario = cursor.fetchone()

   
    if not usuario or not bcrypt.checkpw(senha.encode(), usuario["senha_hash"].encode()):
        return render_template("login.html", erro="E-mail ou senha incorretos.")

    payload = {
        "user_id": usuario["id"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    response = make_response(redirect(url_for('auth.dashboard')))
    
    response.set_cookie('access_token', token, httponly=True)
    
    return response

@auth_bp.route("/dashboard")
def dashboard():
    token = request.cookies.get('access_token')
    
    if not token:
        return redirect(url_for('auth.home'))

    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return render_template("dashboard.html")
    
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        resp = make_response(redirect(url_for('auth.home')))
        resp.delete_cookie('access_token')
        return resp

@auth_bp.route("/logout")
def logout():
    resp = make_response(redirect(url_for('auth.home')))
    resp.delete_cookie('access_token')
    return resp
