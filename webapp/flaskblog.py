from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/login")
def login():
    return render_template('login_signup.html')


@app.route("/signup")
def signup():
    return render_template('login_signup.html')


if __name__ == '__main__':
    app.run(debug=True)
