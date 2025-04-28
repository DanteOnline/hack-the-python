from flask import Flask, render_template, request
import sqlite3
import os
from settings import TABLE_NAME, DB_NAME
from create_db import create_db

create_db()

app = Flask(__name__)
dir_path = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(dir_path, DB_NAME)
connection = sqlite3.connect(DB_NAME, check_same_thread=False)
cursor = connection.cursor()


@app.route('/')
def index():
    username = request.args.get('username')
    result = []
    if username:
        statement = f"SELECT * FROM {TABLE_NAME} where username = '{username}'"
        print(statement)
        cursor.execute(statement)
        result = cursor.fetchall()
    return render_template('index.html', buy=result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8001)

# Простой пример leo' or '1'='1
# Пример эксплуатации leo' union all select sql, 1, 1 FROM sqlite_master where '1'='1
