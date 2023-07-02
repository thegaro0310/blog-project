from flask import Blueprint

main_bp = Blueprint('main', __name__)
blog_bp = Blueprint('blog', __name__)
search_bp = Blueprint('search_results', __name__)

from app.routes import main_routes, blog_routes, search_result_routes
