from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def bgu():
    return redirect("https://in.bgu.ac.il/Pages/default.aspx")


@app.route('/')
def assignment7():
    return 'Assignment 7- flask'


@app.route('/assignment7')
def main():
    return redirect(url_for('assignment7'))


if __name__ == '__main__':
    app.run()
