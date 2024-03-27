from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template('index.html')

@app.route('/', methods=['POST'])
def login():
    user_type = request.form['user_type']
    if user_type == 'customer':
        username = request.form['customer_id']
        password = request.form['password']
        customer = validate_customer(username, password)
        if customer:
            return redirect(url_for('customer_dashboard'))
        else:
            flash('Invalid username or password')
    elif user_type == 'supplier':
        return redirect(url_for('supplier_dashboard'))
    else:
        return "Invalid user type"

if __name__ == '__main__':
    app.run(debug=True)
