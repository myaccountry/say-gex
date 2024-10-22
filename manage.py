import flask
from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/")
def main():
    return render_template('main.html')


@app.route("/reg")
def registration():
    return render_template(f'authorizationPanel/registration.html')


@app.route("/auth")
def authorization():
    return render_template(f'authorizationPanel/login.html')


if __name__ == '__main__':
    app.run(debug=True)
