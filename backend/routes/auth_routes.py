from flask import Blueprint, request, jsonify, render_template
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
    data = request.json
    email = data.get("email")
    senha = data.get("senha")

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE email=%s", (email,))
    usuario = cursor.fetchone()

    if not usuario:
        return jsonify({"erro": "Usuário não encontrado no banco de dados"}), 404
    
    senha_valida = bcrypt.checkpw(senha.encode(), usuario["senha_hash"].encode())

    if not senha_valida:
        return jsonify({"erro": "Senha inválida. Tente novamente."}), 401
    
    playload = {
        "user_id": usuario["id"]
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }

    token = jwt.encode(playload, SECRET_KEY, algorithm="HS256")
    return jsonify({"mensagem": "Login realizado com sucesso!", "token": token})

@auth_bp.route("/dashboard")
def dashboard():
    token = requests.args.get("token")
    if not token:
        return jsonify({"erro": "Token não enviado"}), 401
    
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return render_template("dashboard.html")
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return jsonify({"erro": "Token invalido ou expirado"}), 401
        
