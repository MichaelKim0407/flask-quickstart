from flask import Flask, redirect, request, render_template
from flask_sqlalchemy import SQLAlchemy

__author__ = 'Michael'

# http://flask-sqlalchemy.pocoo.org/2.3/quickstart/
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255))
    from_ = db.Column(db.String(32), name='from')


db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        from_ = request.form['from']
        db.session.add(Message(
            message=message,
            from_=from_,
        ))
        db.session.commit()
        return redirect('/')

    return render_template('index.html', messages=Message.query.all())


@app.route('/clear', methods=['POST'])
def clear():
    Message.query.delete()
    db.session.commit()
    return redirect('/')


@app.route('/init', methods=['POST'])
def init():
    clear()
    header = None
    with open('db.csv') as f:
        for line in f:
            line = line.strip().split(',')
            if header is None:
                header = line
                continue
            db.session.add(Message(
                id=line[0],
                message=line[1],
                from_=line[2],
            ))
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
