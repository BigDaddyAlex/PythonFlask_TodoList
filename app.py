from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String(200),nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

def __repr__(self):
    return '<Task %r>' % self.id

@app.route('/',methods = ['POST','GET'])

def index():
    if request.method == "POST":
        task_content = request.form['content']
        new_task = Todo( content = task_content)
        db.session.add(new_task)
        db.session.commit()
        return redirect('/')
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html',tasks = tasks)

@app.route('/delete/<int:id>')

def delelte(id):
    task_to_delete = Todo.query.get_or_404(id)   
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>',methods = ['POST','GET'])

def update(id):
    if request.method == "POST":
        task_to_update = Todo.query.get_or_404(id)
        task_content = request.form['content']
        task_to_update.content = task_content
        db.session.commit()
        return redirect('/')  
    else:
        task = Todo.query.get_or_404(id)
        return render_template('update.html',task = task)

if __name__ == "__main__":
    app.run(debug = True)


