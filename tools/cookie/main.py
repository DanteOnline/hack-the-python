from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    print('cookie:', request.args)
    return 'hello cookie'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8004)
