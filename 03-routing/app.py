from flask import Flask

__author__ = 'Michael'

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index'


@app.route('/hello')
def hello():
    # http://flask.pocoo.org/docs/1.0/quickstart/#routing
    return 'Hello world!'


@app.route('/res/<res_id>')
# @app.route('/res/<int:res_id>')
def resource(res_id):
    # http://flask.pocoo.org/docs/1.0/quickstart/#variable-rules
    return f"You are requesting resource {res_id}"


if __name__ == '__main__':
    app.run(debug=True)
