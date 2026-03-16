import bcrypt
from database import get_connection


def create_initial_user():

    connection = get_connection()
    cursor = connection.cursor()

    senha = "123456"

    senha_hash = bcrypt.hashpw(
        senha.encode(),
        bcrypt.gensalt()
    ).decode()

    try:

        cursor.execute("""
        INSERT INTO usuarios (nome,email,senha_hash)
        VALUES (%s,%s,%s)
        """, ("Admin", "admin@email.com", senha_hash))

        connection.commit()

    except:
        pass

    connection.close()