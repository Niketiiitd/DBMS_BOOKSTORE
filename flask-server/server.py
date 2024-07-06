import mysql.connector
import threading
from flask import Flask, request, jsonify
from flask_cors import CORS
mydb = mysql.connector.connect(
    host="Nikets-MacBook-Air.local",
    user="root",
    password="Niket@mac",
    database="bookshop", 
    auth_plugin='mysql_native_password'
)
cursor = mydb.cursor()
app = Flask(__name__)
CORS(app)  # Enable CORS


@app.route("/homepage")
def home():
    data = {"heading": "Welcome to the Home Page!"}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
