from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for demonstration
users = {
    'admin': {'password': 'adminpass'},
    'customer': {'password': 'customerpass'},
    'vendor': {'password': 'vendorpass'}
}

@app.route("/")
def index():
    return "Welcome to the main page"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user_type = request.form['user_type']

        if username in users and users[username]['password'] == password:
            # Successful login, redirect to respective homepage
            if user_type == 'admin':
                return redirect(url_for('admin_home'))
            elif user_type == 'customer':
                return redirect(url_for('customer_home'))
            elif user_type == 'vendor':
                return redirect(url_for('vendor_home'))
            else:
                return "Invalid user type"
        else:
            return "Invalid username or password"
    return render_template('login.html')

@app.route("/admin")
def admin_home():
    return "Welcome to the Admin Homepage"

@app.route("/customer")
def customer_home():
    return "Welcome to the Customer Homepage"

@app.route("/vendor")
def vendor_home():
    return "Welcome to the Vendor Homepage"

if __name__ == '__main__':
    app.run(debug=True)
