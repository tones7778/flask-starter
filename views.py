# project/views.py
# refactor --> get rid of the delete links and create a delete button, and check boxes.

import sqlite3
from functools import wraps

from forms import AddTaskForm
from flask import Flask, flash, redirect, render_template, \
    request, session, url_for, g


# config

app = Flask(__name__)
app.config.from_object('_config')


# helper functions

def connect_db():
    return sqlite3.connect(app.config['DATABASE_PATH'])


# route handlers

@app.route('/', methods=['GET', 'POST'])
def login():
 
    session['logged_in'] = True
    flash('Welcome!')
    return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/tasks/')
def tasks():
    g.db = connect_db()
    cur = g.db.execute('select name, food_item, comments, potluck_id from potluck')
    open_tasks = [dict(name=row[0], food_item=row[1], comments=row[2], potluck_id=row[3]) for row in cur.fetchall()]
    g.db.close()
    return render_template('tasks.html', form=AddTaskForm(request.form), open_tasks=open_tasks)


# Add new tasks
@app.route('/add/', methods=['POST'])
def new_task():
    g.db = connect_db()
    name = request.form['name']
    food_item = request.form['food_item']
    comments = request.form['comments']
    if not name or not food_item or not comments:
        flash("All fields are required. Please try again.")
        return redirect(url_for('tasks'))
    else:
        g.db.execute('insert into potluck (name, food_item, comments) \
            values (?, ?, ?)', [
                request.form['name'],
                request.form['food_item'],
                request.form['comments']
            ]
        )
        g.db.commit()
        g.db.close()
        flash('New entry was successfully posted. Thanks.')
        return redirect(url_for('tasks'))



# Delete Tasks
@app.route('/delete/<int:potluck_id>/')
def delete_entry(potluck_id):
    g.db = connect_db()
    g.db.execute('delete from potluck where potluck_id='+str(potluck_id))
    g.db.commit()
    g.db.close()
    flash('The task was deleted.')
    return redirect(url_for('tasks'))

@app.route("/map")
def map():
    return render_template("map.html")