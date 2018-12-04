from flask import Flask, render_template

__author__ = 'Michael'

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', pages=range(10))


@app.route('/<int:i>')
def page(i):
    return render_template('page.html', i=i, pages=range(10))


if __name__ == '__main__':
    app.run(debug=True)
