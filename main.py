from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)
class Todo(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100))
    content=db.Column(db.String(300))
    iscomplete=db.Column(db.Boolean)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tasks')
def tasks():
	return render_template('task.html')
if __name__ == '__main__':
    app.run(debug=True)
