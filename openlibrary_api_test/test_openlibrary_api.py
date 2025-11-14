import pytest
from api_client import (
    get_olid,
    read_search_authors_json,
    read_api_books,
    read_authors,
    read_authors_works)

def test_get_olid_valid():
    olid = get_olid("richard feynman")
    assert olid.startswith("OL")

def test_get_olid_invalid():
    olid = get_olid("nonexistent author 123")
    assert olid == "Author not found"

def test_read_search_authors_json():
    res = read_search_authors_json("feynman")
    assert res.status_code == 200
    assert "docs" in res.json()

def test_read_api_books():
    res = read_api_books("1-4292-0124-X")
    assert res.status_code == 200
    assert isinstance(res.json(), dict)

def test_read_authors():
    olid = get_olid("h c verma")
    if olid != "Author not found":
        res = read_authors(olid.replace("/authors/", ""))
        assert res.status_code == 200
        assert "name" in res.json()

def test_read_authors_works():
    olid = get_olid("r d sharma")
    if olid != "Author not found":
        res = read_authors_works(olid.replace("/authors/", ""), 2)
        assert res.status_code == 200
        assert "entries" in res.json()