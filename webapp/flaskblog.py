from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_type = request.form.get("user_type")
        if user_type == "customer":
            return redirect(url_for("customer"))
        # Add similar conditions for other user types if needed
    return render_template('login_signup.html')

@app.route("/customer")
def customer():
    return render_template('customer.html')

if __name__ == '__main__':
    app.run(debug=True)
