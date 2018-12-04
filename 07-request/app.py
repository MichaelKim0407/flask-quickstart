from flask import Flask, render_template, request, redirect

__author__ = 'Michael'

app = Flask(__name__)

messages = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        messages.append(message)
        return redirect('/')

    return render_template('index.html', messages=messages)


@app.route('/clear', methods=['POST'])
def clear():
    messages.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
