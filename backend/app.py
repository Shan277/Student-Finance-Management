from flask import Flask, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="799277",
    database="register_db"
)



@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()
    print("DATA RECEIVED:", data)

    if not data:
        return "No data received", 400

    username = data["username"]
    password = data["password"]

    print(username, password)
    
    cursor = db.cursor()
    
    cursor.execute("insert into users(name,password) values(%s,%s)", (username,password))
    db.commit()
    cursor.close()
    
    return "Registered Successfully"

if __name__ == "__main__":
    app.run(debug=True)