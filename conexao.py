import psycopg2

def conectar():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Unip@r123",
        port="5433",
        options="-c client_encoding=UTF8"
    )