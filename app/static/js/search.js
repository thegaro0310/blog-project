// search.js

function performSearch(query) {
    const searchResultsContainer = document.getElementById('search-results');
    searchResultsContainer.innerHTML = '';
  
    if (query.trim() === '') {
      const noQueryMessage = document.createElement('p');
      noQueryMessage.textContent = 'Please enter a search query.';
      searchResultsContainer.appendChild(noQueryMessage);
      return;
    }
  
    const searchResults = getSearchResults(query);
  
    if (searchResults.length === 0) {
      const noResultsMessage = document.createElement('p');
      noResultsMessage.textContent = 'No blogs found.';
      searchResultsContainer.appendChild(noResultsMessage);
      return;
    }
  
    searchResults.forEach((result) => {
      const postLink = document.createElement('a');
      postLink.textContent = result.title;
      postLink.href = `/post/${result.id}`;
      searchResultsContainer.appendChild(postLink);
      searchResultsContainer.appendChild(document.createElement('br'));
    });
  }
  
  function getSearchResults(query) {
    // Replace this with your own logic to fetch blog data from the server
    // For example, you can make an AJAX request to an API endpoint on the server
  
    // Dummy blog data for demonstration purposes
    const blogData = [
      { id: 1, title: 'Blog Post 1' },
      { id: 2, title: 'Blog Post 2' },
      { id: 3, title: 'Blog Post 3' },
      { id: 4, title: 'Blog Post 4' },
      { id: 5, title: 'Blog Post 5' },
    ];
  
    const searchResults = blogData.filter((blog) =>
      blog.title.toLowerCase().includes(query.toLowerCase())
    );
  
    return searchResults;
  }
  
  // Event listener for the search input
  const searchInput = document.getElementById('search-input');
  searchInput.addEventListener('input', () => {
    const query = searchInput.value;
    performSearch(query);
  });
  