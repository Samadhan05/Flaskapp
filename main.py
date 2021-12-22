from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(300))
    iscomplete = db.Column(db.Boolean)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add-task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        new_task = Todo(
            title=request.form['title'],
            content=request.form['content'],
            iscomplete=0
        )

        db.session.add(new_task)
        db.session.commit()
        
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/tasks')
def tasks():
    return render_template('task.html')


if __name__ == '__main__':
    app.run(debug=True)
