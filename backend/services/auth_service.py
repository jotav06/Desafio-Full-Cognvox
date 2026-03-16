import bcrypt
import jwt
import datetime
import os
from dotenv import load_dotenv
from database import get_connection

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")


def autenticar_usuario(email, senha):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM usuarios WHERE email=%s",
        (email,)
    )

    usuario = cursor.fetchone()
    conn.close()

    if not usuario:
        return None

    if not bcrypt.checkpw(
        senha.encode(),
        usuario["senha_hash"].encode()
    ):
        return None

    return usuario


def gerar_token(user_id):

    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.now(datetime.timezone.utc)
        + datetime.timedelta(hours=1)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )

    return token