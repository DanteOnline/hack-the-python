import os
import sqlite3
from settings import DB_NAME

def create_db():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    db_name = os.path.join(dir_path, DB_NAME)
    con = sqlite3.connect(db_name)
    cur = con.cursor()

    DB_SQL = 'create_db.sql'
    db_sql = os.path.join(dir_path, DB_SQL)

    with open(db_sql, 'r') as f:
        text = f.read()
    cur.executescript(text)
    cur.close()
    con.close()


if __name__ == '__main__':
    create_db()
