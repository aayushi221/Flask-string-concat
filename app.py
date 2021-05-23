from html import escape

from flask import Flask, redirect

app = Flask(__name__)

strings = ''


@app.route('/')
def hello_world():
    return 'You might wanna add a name in the URL up there!'


@app.route('/<string:s>')
def concat_and_return(s):
    global strings
    if s != 'favicon.ico':
        strings += escape(s) + " "
    redirect('/')
    return strings


if __name__ == '__main__':
    app.run()