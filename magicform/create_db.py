import sqlite3
from settings import DB_NAME

con = sqlite3.connect(DB_NAME)
cur = con.cursor()
with open('create_db.sql', 'r') as f:
    text = f.read()
cur.executescript(text)
cur.close()
con.close()
