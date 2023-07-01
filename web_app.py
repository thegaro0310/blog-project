from flask import Flask, render_template, request, redirect, url_for, flash 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    author = db.Column(db.String(50))
    views = db.Column(db.Integer, default=0)
    date = db.Column(db.DateTime, default=datetime.utcnow)

app.app_context().push()
db.create_all()

app.secret_key = 'your_secret_key_here'
@app.route('/')
def index():
    posts = Post.query.order_by(Post.date.desc()).all()
    if not posts:
        message = "Welcome to my blog site, let write some new blogs"
        return render_template('index.html', message=message)
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get(post_id)
    if post:
        post.views += 1
        db.session.commit()
        return render_template('post.html', post=post)
    else:
        return redirect('/')

@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']

        new_post = Post(title=title, content=content, author=author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/')
    return render_template('add_post.html')

@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return redirect('/')
    
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        post.author = request.form['author']
        db.session.commit()
        return redirect(f'/post/{post_id}')
    
    return render_template('edit_post.html', post=post)

@app.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

