from flask import Flask, redirect, jsonify, render_template, request, g, session
from flask_session import Session
from tempfile import mkdtemp
import sqlite3

app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
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
    with app.app_context():
        db = get_db()
        cur = get_db().execute(query, args)
        rv = cur.fetchall()
        db.commit()
        cur.close()
        return (rv[0] if rv else None) if one else rv

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('Initialized the database.')

@app.route("/logout")
def logout():
    session.clear()
    return render_template("/")

@app.route("/login")
def login():
    print("\n\n" + request.args.get("id"))
    session["user_id"] = request.args.get("id")
    print(session["user_id"])
    return render_template("/")

# Routes
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        course = request.form.get("course")
        students = query_db("SELECT name FROM students LEFT JOIN courses ON students.id=courses.student WHERE courses.title=?", [course])
        print(students)
        return render_template("index.html", students=students, course=course)
    else:
        return render_template("index.html")

@app.route("/addCourses", methods=['GET', 'POST'])
def addCourses():
    if request.method == "POST":
        print("hello")
        name = request.form.get('name')
        if not name:
            return redirect("/addCourses")
        courses = request.form.get('courses')
        if not courses:
            return redirect("/addCourses")
        query_db("insert into students (name) values (?)", [name])
        studentId = query_db("select id from students where name=?", [name])
        print(studentId[0][0])
        for course in courses.replace(" ", "").split(","):
            query_db("insert into courses (title, student) values (?, ?)", [course, int(studentId[0][0])])
        print(query_db("SELECT * FROM students"))
        print(query_db("SELECT * FROM courses"))
        return redirect("/")
    else:
        return render_template("addCourses.html")
