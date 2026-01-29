from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'frontend'))
app.secret_key = os.getenv("SECRET_KEY", "smartassess_secret")

# ---------- DATABASE ----------
def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root"),
        database=os.getenv("DB_NAME", "smartassess")
    )

def fetch_assessments():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT assessment_name, skills FROM assessments")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

# ---------- ROUTES ----------
@app.route("/")
def landing():
    return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]

        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (fullname, email, password) VALUES (%s,%s,%s)",
            (fullname, email, password)
        )
        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for("login"))

    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s",
            (email, password)
        )
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            session["user"] = email
            return redirect(url_for("recommend_page"))
        else:
            return render_template("login-error.html")

    return render_template("login.html")

@app.route("/recommend-page")
def recommend_page():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("recommend.html", query="")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)