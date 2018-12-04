from flask import Flask, render_template, request, redirect, jsonify

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


@app.route('/api', methods=['GET'])
def api():
    format = request.args.get('format')
    if format == 'json':
        return jsonify(messages)
    elif format == 'html':
        return '<br>'.join(messages)
    else:
        return '\n'.join(messages)


if __name__ == '__main__':
    app.run(debug=True)
