from flask import Flask, request, session ,redirect, url_for
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)
app.secret_key = "secret123"

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
        return "No data received"

    username = data["username"]
    password = data["password"]
    email = data["email"]

    print(username, password, email)
    
    cursor = db.cursor()
    
    cursor.execute("select * from users where name = %s", (username,))
    user = cursor.fetchone() #returns none if not found #list datatype
    print("USER FOUND:", user)
    if user!= None:
        return "Username already exists"
    

    cursor.execute("insert into users(name,password,email) values(%s,%s,%s)", (username,password,email) )
    db.commit()
    cursor.close()
    
    session["user"] = username
    
    return "Registered Successfully"

if __name__ == "__main__":
    app.run(debug=True)