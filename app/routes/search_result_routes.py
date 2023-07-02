from flask import Blueprint, render_template, request
from app.models import Post

search_results_bp = Blueprint('search_results', __name__)

def fetch_search_results(search_query):
    # Implement your search logic here
    # Query the database or perform any other search operations based on the search_query
    # Return the search results
    
    # For demonstration purposes, let's assume you are querying the 'Post' model for title matches
    search_results = Post.query.filter(Post.title.ilike(f'%{search_query}%')).all()
    return search_results

@search_results_bp.route('/search_results')
def search_results():
    search_query = request.args.get('query', '')
    
    # Perform the search operation based on the search_query
    search_results = fetch_search_results(search_query)

    return render_template('search_results.html', search_query=search_query, search_results=search_results)
