from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        text = request.form['formula']
        try:
            result = eval(text)
        except (SyntaxError, NameError):
            result = 'Error: wrong input'
        return render_template('index.html', result=result, text=text)


@app.route('/protected/', methods=['GET', 'POST'])
def index_protected():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        text = request.form['formula']
        try:
            result = eval(text)
        except (SyntaxError, NameError):
            result = 'Error: wrong input'
        return render_template('index.html', result=result, text=text)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8003)
