import json
from flask import Flask, redirect, request, render_template
from flask_pymongo import PyMongo

__author__ = 'Michael'

# https://flask-pymongo.readthedocs.io/en/latest/
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/messages_db"
db = PyMongo(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        from_ = request.form['from']
        db.db.messages.insert_one({
            'message': message,
            'from': from_
        })
        return redirect('/')

    return render_template('index.html', messages=db.db.messages.find())


@app.route('/clear', methods=['POST'])
def clear():
    db.db.messages.delete_many({})
    return redirect('/')


@app.route('/init', methods=['POST'])
def init():
    clear()
    with open('db.json') as f:
        data = json.load(f)
        db.db.messages.insert_many(data)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
