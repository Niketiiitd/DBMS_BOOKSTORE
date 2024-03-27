from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/login")
def login():
    return render_template('templates/login_signup.html')  # Adjust the path


@app.route("/signup")
def signup():
    return render_template('templates/login_signup.html')  # Adjust the path


if __name__ == '__main__':
    app.run(debug=True)
