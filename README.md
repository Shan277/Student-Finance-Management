# 🔐 Flask Login System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-F29111?style=for-the-badge&logo=mysql&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

A full-stack authentication system built with **Flask**, **MySQL**, and **Vanilla JavaScript** — featuring user registration, login, session management, and protected routes.

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [How It Works](#how-it-works)
- [Security Notes](#security-notes)

---

## ✨ Features

- User registration with username, password, and email
- Secure login with session-based authentication
- Protected dashboard — redirects unauthenticated users to login
- Logout functionality with session cleanup
- Duplicate username detection on registration
- Cross-origin support via Flask-CORS

---

## 🛠 Tech Stack

| Layer    | Technologies |
|----------|-------------|
| Backend  | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white) ![Flask-CORS](https://img.shields.io/badge/Flask--CORS-lightgrey?style=flat-square) |
| Database | ![MySQL](https://img.shields.io/badge/MySQL-F29111?style=flat-square&logo=mysql&logoColor=white) ![mysql-connector](https://img.shields.io/badge/mysql--connector-blue?style=flat-square) |
| Frontend | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) |
| Auth     | ![Sessions](https://img.shields.io/badge/Flask_Sessions-cookie--based-green?style=flat-square) |

---

## 📁 Project Structure

```
project/
│
├── app.py                  # Flask backend — routes & session logic
│
├── index.html              # Login & Register page
├── dashboard.html          # Protected dashboard page
│
├── javascript/
│   ├── index.js            # Login/Register form handlers
│   └── dashboard.js        # Auth check & logout logic
│
└── css/
    └── index.css           # Styles for login/register page
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- MySQL Server
- Node.js (optional, for local dev server)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install Python Dependencies

```bash
pip install flask flask-cors mysql-connector-python
```

### 3. Set Up the Database

Open your MySQL client and run:

```sql
CREATE DATABASE register_db;

USE register_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL
);
```

### 4. Configure Database Credentials

In `app.py`, update the database connection with your credentials:

```python
db = mysql.connector.connect(
    host="localhost",
    user="your_mysql_user",
    password="your_mysql_password",
    database="register_db"
)
```

### 5. Run the Flask Server

```bash
python app.py
```

The backend will start at `http://127.0.0.1:5000`.

### 6. Open the Frontend

Open `index.html` in your browser directly, or serve it with a local server:

```bash
# Using Python's built-in server
python -m http.server 3000
```

Then visit `http://localhost:3000`.

---

## 📡 API Endpoints

| Method | Endpoint        | Description                              |
|--------|-----------------|------------------------------------------|
| POST   | `/login`        | Authenticate user, create session        |
| POST   | `/register`     | Register new user, create session        |
| GET    | `/check_login`  | Returns `"OK"` if user session is active |
| GET    | `/logout`       | Clears user session                      |

### Request & Response Examples

**POST `/register`** — JSON body:
```json
{
  "username": "john_doe",
  "password": "mypassword",
  "email": "john@example.com"
}
```

**POST `/login`** — form data:
```
username=john_doe&password=mypassword
```

---

## ⚙️ How It Works

1. **Registration** — The user submits a form; the frontend sends a `POST` request with JSON. Flask checks for duplicate usernames, inserts the new user into MySQL, and saves the username in a server-side session.

2. **Login** — The user submits credentials as form data. Flask queries the database and, if matched, stores the username in the session.

3. **Session Check** — On every page load, `dashboard.js` calls `/check_login`. If the session is missing, the user is redirected back to `index.html`.

4. **Logout** — The session is cleared server-side and the user is redirected to the login page.

---

## 🔒 Security Notes

> This project is intended for **learning purposes**. Before deploying to production, consider the following improvements:

- **Hash passwords** — use `bcrypt` or `werkzeug.security` instead of storing plain-text passwords
- **Use HTTPS** — protect session cookies and credentials in transit
- **Strengthen the secret key** — replace `"secret123"` with a long, random secret (e.g., `os.urandom(24)`)
- **Use environment variables** — store DB credentials and secret keys in a `.env` file, not in source code
- **Add input validation** — sanitize and validate all user inputs on the backend
- **Parameterized queries** — already in use ✅ (protects against SQL injection)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
