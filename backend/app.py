from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()
    print("DATA RECEIVED:", data)

    if not data:
        return "No data received", 400

    username = data["username"]
    password = data["password"]

    print(username, password)

    return "Registered Successfully"

if __name__ == "__main__":
    app.run(debug=True)