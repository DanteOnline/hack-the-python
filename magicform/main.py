from flask import Flask, render_template, request, redirect
import sqlite3
from settings import TABLE_NAME, DB_NAME
import os

app = Flask(__name__)
dir_path = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(dir_path, DB_NAME)
connection = sqlite3.connect(DB_NAME, check_same_thread=False)
cursor = connection.cursor()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':

        statement = f"SELECT * FROM {TABLE_NAME}"
        cursor.execute(statement)
        result = cursor.fetchall()
        return render_template('index.html', comments=result)
    else:
        name = request.form['name']
        text = request.form['text']
        statement = f"insert into {TABLE_NAME}(name,text) values (?,?)"
        cursor.execute(statement, (name, text))
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8002)
