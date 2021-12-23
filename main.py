
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Create database
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(300))
    iscomplete = db.Column(db.Boolean)

# Only run once database has been created
# db.create_all()



@app.route('/')
def home():
    todo_list = Todo.query.all()
    return render_template("index.html", tasks=todo_list)


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
	return render_template('task.html',tasks=tasks)



if __name__ == '__main__':
    app.run(debug=True)
