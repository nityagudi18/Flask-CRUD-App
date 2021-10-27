import sqlite3


def connect():
    conn = sqlite3.connect('database/userstore.db')
    cursor = conn.cursor()
    return conn, cursor


def create_table():
    conn, cursor = connect()
    cursor.execute('''CREATE TABLE USERS
         (ID INTEGER PRIMARY KEY AUTOINCREMENT,
         USERNAME        TEXT    NOT NULL,
         PASSWORD        TEXT     NOT NULL);''')
    conn.commit()
    cursor.close()


def write_record(statement):
    conn, cursor = connect()
    cursor.execute(statement)
    conn.commit()
    cursor.close()


def read_records(statement):
    conn, cur = connect()
    cur.execute(statement)
    ret = cur.fetchall()
    cur.close()
    return ret


def delete_records():
    conn, cur = connect()
    cur.execute("""DELETE FROM USERS WHERE ID=3""")
    conn.commit()
    cur.close()
