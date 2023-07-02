from flask import Blueprint, render_template
from app import db
from app.models import Post

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    posts = Post.query.order_by(Post.date.desc()).all()
    if not posts:
        message = "Welcome to my blog site. Let's write some new blogs!"
        return render_template('index.html', message=message)
    return render_template('index.html', posts=posts)
