import mysql.connector
import bcrypt


def create_database():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jv0602fs@"
    )

    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS login_cognvox")

    connection.close()


def get_connection():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jv0602fs@",
        database="login_cognvox"
    )

    return connection


def create_tables():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        email VARCHAR(100) UNIQUE,
        senha_hash VARCHAR(255)
    )
    """)

    connection.commit()
    connection.close()


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