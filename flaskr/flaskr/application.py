from flask import Flask, redirect, render_template, request, g
import sqlite3

app = Flask(__name__)

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
        name = request.form.get('username')
        if not name:
            return redirect("/addCourses")
        courses = request.form.get('courses')
        if not courses:
            return redirect("/addCourses")
        query_db("INSERT INTO students (name) VALUES (?)", [name])
        studentId = query_db("SELECT id FROM students WHERE name=?", [name])
        for course in classes.replace(" ", "").split(","):
            query_db("INSERT INTO courses (title, student) VALUES (?, ?)", [course, studentId])
        print(query_db("SELECT * FROM students"))
        print(query_db("SELECT * FROM courses"))
        return redirect("/")
    else:
        return render_template("addCourses.html")
