import pytest
from api_client import (
    author_detail,
    get_olid,
    read_search_authors_json,
    read_api_books,
    read_authors,
    read_authors_works)

def test_get_olid_valid():
    olid = get_olid("Richard Feynman")
    assert olid.startswith("OL")

def test_get_olid_invalid():
    olid = get_olid("nonexistent author 123")
    assert olid == "Author not found"



@pytest.mark.parametrize("author",["H. C. Verma","R. D. Sharma","Yashavant Kanetkar","Richard Feynman"])
def test_vaid_author_detail(author):
    response=author_detail(author)
    assert "application/json" in response.headers.get("Content-Type",""),"Header does not indicate JSON"
    try:
        data = response.json()
        assert data != None ,"Parsed JSON is None"
    except:
        assert False ,"Response body is not JSON"
        
    assert response.json()['numFound'] >0 ,"ERRROR : Unexpected number of authors in positive test"
    assert response.json()['docs'][0]['name'] == author,"ERROR: Author name didn't match in positive test"
    assert response.status_code == 200,"UNEXPECTED STATUS CODE" 



@pytest.mark.parametrize("author",["","$","No_author"])
def test_invaid_author_detail(author):
    response=author_detail(author)
    assert "application/json" in response.headers.get("Content-Type",""),"Header does not indicate JSON"
    try:
        data = response.json()
        assert data != None ,"Parsed JSON is None"
    except:
        assert False ,"Response body is not JSON"
    assert response.json()['numFound']==0 ,"ERRROR : Unexpected number of authors in negative test"
    assert response.status_code == 200,"UNEXPECTED STATUS CODE" 


#
def test_read_search_authors_json():
    res = read_search_authors_json("feynman")
    assert res.status_code == 200
    assert "docs" in res.json()


#Any api request with invalid/not available isbn number will simply throw error
@pytest.mark.parametrize("isbn",["1-4292-0124-X"])
def test_read_api_books(isbn):
    res = read_api_books(isbn)
    #assert isinstance(res.json(), dict)
    assert "application/json" in res.headers.get("Content-Type",""),"Header does not indicate JSON"
    try:
        data = res.json()
        assert data != None ,"Parsed JSON is None"
    except:
        assert False ,"Response body is not JSON"
    assert res.status_code == 200



@pytest.mark.parametrize("author",["H. C. Verma","R. D. Sharma","Yashavant Kanetkar","Richard Feynman"])
def test_read_valid_authors(author):
    olid = get_olid(author)
    if olid != "Author not found":
        res = read_authors(olid.replace("/authors/", ""))
        
    assert "application/json" in res.headers.get("Content-Type",""),"Header does not indicate JSON"
    try:
        data = res.json()
        assert data != None ,"Parsed JSON is None"
    except:
        assert False ,"Response body is not JSON"


    assert res.json()['name'] == author
    assert res.status_code == 200



@pytest.mark.parametrize("author",["H. C. Verma","R. D. Sharma","Yashavant Kanetkar","Richard Feynman"])
def test_read_authors_works(author):
    olid = get_olid(author)
    if olid != "Author not found":        
        res = read_authors_works(olid.replace("/authors/", ""), 2)
        assert "application/json" in res.headers.get("Content-Type",""),"Header does not indicate JSON"
        try:
            data = res.json()
            assert data != None ,"Parsed JSON is None"
        except:
            assert False ,"Response body is not JSON"
                
        assert "entries" in res.json()
        assert res.json()['links']['author'] == '/authors/'+olid
        assert res.status_code == 200