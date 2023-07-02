from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Post
from datetime import datetime

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get(post_id)
    if post:
        post.views += 1
        db.session.commit()
        return render_template('post.html', post=post)
    else:
        return redirect('/')

@blog_bp.route('/add_post', methods=['GET', 'POST'])
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

@blog_bp.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
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

@blog_bp.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('main.index'))
