import requests

# Set the base URL for the Open Library API
base_url = "http://openlibrary.org/search.json"

# Set the parameters for the book search
params = {
    "title": "Plato's republic",
    "limit": 1  # Limit the results to 1 book
}

# Make a request to the Open Library API
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract the book information
    if "docs" in data and len(data["docs"]) > 0:
        book_info = data["docs"][0]
        if "title" in book_info:
            title = book_info["title"]
            print(f"Title: {title}")
        if "author_name" in book_info:
            authors = ", ".join(book_info["author_name"])
            print(f"Authors: {authors}")
        if "key" in book_info:
            open_library_key = book_info["key"]
            print(f"Open Library Key: {open_library_key}")
    else:
        print("No results found for The Prophet")
else:
    print(f"Failed to retrieve book information. Status code: {response.status_code}")