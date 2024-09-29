import requests

# Set the base URL for the Google Books API
base_url = "https://www.googleapis.com/books/v1/volumes"

# Set the parameters for the book search
params = {
    "q": "The Prophet",
    "maxResults": 1  # Limit the results to 1 book
}

# Make a request to the Google Books API
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract the web reader link for the book
    if "items" in data and len(data["items"]) > 0:
        book_info = data["items"][0]["volumeInfo"]
        if "title" in book_info:
            title = book_info["title"]
            print(f"Title: {title}")
        if "authors" in book_info:
            authors = ", ".join(book_info["authors"])
            print(f"Authors: {authors}")
        if "webReaderLink" in book_info:
            web_reader_link = book_info["webReaderLink"]
            print(f"Web Reader Link: {web_reader_link}")
        if "key" in book_info:
            open_library_key = book_info["key"]
            print(f"Open Library Key: {open_library_key}")
    else:
        print("No results found for the 48 Laws of Power")
else:
    print(f"Failed to retrieve book information. Status code: {response.status_code}")