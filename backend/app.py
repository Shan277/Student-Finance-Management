from flask import Flask, request, session ,redirect, url_for
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app, supports_credentials=True) #allows cross-origin requests with credentials (cookies, authorization headers, etc.)
app.secret_key = "secret123"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="799277",
    database="register_db"
)


@app.route("/login", methods=["POST"])

def login():
    
    username = request.form["username"]
    password = request.form["password"]
    
    cursor = db.cursor()
    cursor.execute("select * from users where name = %s and password = %s", (username,password))
    user = cursor.fetchone()
    print(user)
    
    if user == None:
        return "Invalid username or password"
    
    
    session["user"] = username 
    return "Login successful"




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
    
    session["user"] = username #saves user in browser session session = {"user": "username"}
    
    return "Registered Successful"



@app.route("/check_login")
def check_login():
    if "user" in session: #checks if user is logged in by checking if "user" exists in session dictionary
        print("USER IN SESSION:", session["user"])
        return "OK"
    print("NO USER IN SESSION")
    return "NO"


if __name__ == "__main__":
    app.run(debug=True)