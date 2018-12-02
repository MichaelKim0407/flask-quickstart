from flask import Flask, render_template, abort

__author__ = 'Michael'

app = Flask(__name__)

RESOURCES = [
    {
        'id': 1,
        'name': 'Name',
        'value': 'Bob',
    },
    {
        'id': 2,
        'name': 'Age',
        'value': 20,
    },
    {
        'id': 3,
        'name': 'Occupation',
        'value': 'Student',
    },
    {
        'id': 4,
        'name': 'Favorite color',
        'value': 'Green',
    },
]


@app.route('/')
def index():
    # http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates
    return render_template('index.html', resources=RESOURCES)


@app.route('/res/<int:res_id>')
def resource(res_id):
    for res in RESOURCES:
        if res['id'] == res_id:
            return render_template('resource.html', res=res)
    abort(404)


if __name__ == '__main__':
    app.run(debug=True)
