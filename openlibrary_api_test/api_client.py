import requests

BASE_URL = "https://openlibrary.org"

def get_olid(author_name: str) -> str:
    params = {"q": author_name}
    response = requests.get(f"{BASE_URL}/search/authors.json", params=params)
    if response.status_code == 200 and response.json().get('docs'):
        return response.json()['docs'][0]['key']
    return "Author not found"

def read_search_authors_json(query: str):
    headers = {'accept': 'application/json'}
    params = {'q': query}
    return requests.get(f"{BASE_URL}/search/authors.json", params=params, headers=headers)

def read_api_books(isbn: str):
    params = {
        'bibkeys': f'ISBN:{isbn}',
        'format': 'json',
        'jscmd': 'viewapi'
    }
    return requests.get(f"{BASE_URL}/api/books", params=params)

def read_authors(olid: str):
    headers = {'accept': 'application/json'}
    return requests.get(f"{BASE_URL}/authors/{olid}.json", headers=headers)

def read_authors_works(olid: str, limit: int):
    headers = {'accept': 'application/json'}
    return requests.get(f"{BASE_URL}/authors/{olid}/works.json?limit={limit}", headers=headers)