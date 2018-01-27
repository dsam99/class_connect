from flask import Flask, flash, redirect, redirect, render_template, request, session, jsonify, url_for, g
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

#From tutorial
import os
import sqlite3


# Configure application
app = Flask(__name__)
app.config.from_object(__name__) #load config from this file

app.config.update(dict(
	DATABASE=os.path.join(app.root_path,'flaskr.db'),
	SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
	))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# Connecting database
def connect_db():
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv

# Connect to database
def get_db():
	"""Open new database connections"""
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

# Disconnect from database
@app.teardown_appcontext
def close_db(error):
	"""Closes the database at the end of request"""
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')



# Home page
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addclasses", methods=['GET', 'POST'])
def results():
    return render_template("addclasses.html")

