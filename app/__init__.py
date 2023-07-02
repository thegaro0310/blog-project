from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    app.secret_key = 'your_secret_key_here'
    
    db.init_app(app)
    
    from app.routes.main_routes import main_bp
    from app.routes.blog_routes import blog_bp
    from app.routes.search_result_routes import search_results_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(blog_bp)
    app.register_blueprint(search_results_bp)
    
    with app.app_context():
        db.create_all()
    
    return app
