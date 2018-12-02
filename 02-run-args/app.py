from flask import Flask

__author__ = 'Michael'

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world!'


if __name__ == '__main__':
    # http://flask.pocoo.org/docs/1.0/api/#flask.Flask.run
    app.run(debug=True)
    # app.run(port=5001)
    # app.run(host='0.0.0.0')
