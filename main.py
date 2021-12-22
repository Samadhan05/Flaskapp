from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)
class Todo(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100))
    content=db.Column(db.String(300))
    iscomplete=db.Column(db.Boolean)

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    print("\nTask:",task)
    if request.method == 'POST':
        task.title = request.form['Title']
        task.content = request.form['Content']


        try:
            db.session.commit()
            return redirect('/')
        except:
            return "connot update the task"
    else:
        return render_template('update.html', task=task)
@app.route('/')
def home():
    todo_list = Todo.query.all()
    return render_template("index.html", tasks=todo_list)

@app.route('/tasks')
def tasks():
	return render_template('task.html',tasks=tasks)
if __name__ == '__main__':
    app.run(debug=True)
