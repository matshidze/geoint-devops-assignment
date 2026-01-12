import os
import time
import psycopg2
from flask import Flask, request, render_template, redirect, url_for, flash
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret")

# Database config from environment
DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "geointdb")
DB_USER = os.getenv("DB_USER", "geointuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "geointpass")

# Prometheus metrics (unique names to avoid duplication)
REQUEST_COUNT = Counter(
    "geoint_http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "geoint_http_request_latency_seconds",
    "HTTP request latency in seconds",
    ["endpoint"]
)

def get_conn():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )

def init_db():
    conn = get_conn()
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS submissions (
                id SERIAL PRIMARY KEY,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT NOW()
            );
        """)
    conn.close()

@app.before_request
def ensure_db():
    if not getattr(app, "_db_initialized", False):
        init_db()
        app._db_initialized = True

@app.route("/", methods=["GET"])
def index():
    start = time.time()
    status = 200
    try:
        conn = get_conn()
        with conn.cursor() as cur:
            cur.execute("SELECT id, message, created_at FROM submissions ORDER BY id DESC LIMIT 20;")
            rows = cur.fetchall()
        conn.close()
        return render_template("index.html", rows=rows)
    finally:
        REQUEST_COUNT.labels("GET", "/", str(status)).inc()
        REQUEST_LATENCY.labels("/").observe(time.time() - start)

@app.route("/submit", methods=["POST"])
def submit():
    start = time.time()
    status = 500
    try:
        message = (request.form.get("message") or "").strip()
        if not message:
            flash("Message cannot be empty.", "error")
            status = 400
            return redirect(url_for("index"))

        conn = get_conn()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO submissions (message) VALUES (%s);", (message,))
        conn.commit()
        conn.close()

        flash("Saved successfully!", "success")
        status = 302
        return redirect(url_for("index"))
    finally:
        REQUEST_COUNT.labels("POST", "/submit", str(status)).inc()
        REQUEST_LATENCY.labels("/submit").observe(time.time() - start)

@app.route("/metrics", methods=["GET"])
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    host = os.getenv("APP_HOST", "0.0.0.0")
    port = int(os.getenv("APP_PORT", "5000"))
    app.run(host=host, port=port)
