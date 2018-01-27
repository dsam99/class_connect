from flask import Flask, flash, redirect, render_template, request, session, jsonify, url_for, g
import sqlite3
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Database
DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# Routes
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        return render_template("addclasses.html")
    else:
        return render_template("index.html")

@app.route("/addclasses", methods=['GET', 'POST'])
def addclasses():
    if request.method == "POST":
        name = request.form.get('user_name')
        classes = request.form.get('classes_taken')
        query_db("insert into students (name) values (?)", [name])
        for course in classes.replace(" ", "").split(","):
            query_db("insert into courses (title, student) values (?, ?)", [course, name])
        print(query_db("select * from students"))
        return render_template("index.html")
    else:
        return render_template("addclasses.html")
