import pytest
import pytest_check as check
from selenium import webdriver
from BasePage import ProjectGutenberg
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import requests as rq

class TestLogin:
    @pytest.fixture(scope="function", autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.gutenberg.org")
        self.page=ProjectGutenberg(self.driver)
        yield
        self.driver.quit()


    def test_search_bar(self):
        print("\n\n\n\n")
        self.page.search("The Roman hat mystery by Ellery Queen")
        print(self.page.get_title())
        assert "The Roman hat mystery by Ellery Queen" in  self.page.get_title() ,"ERROR in test_search_bar"
    
    
    def test_visibility_of_common_elements(self):
        print("\n\n\n\n")
        d1=self.page.__dict__
        for i in d1:
            if i=='driver':
                continue
            if check.is_true(self.page.get_common_element(i) != None,i+" not found!") :
                print(i,"<-----This element is visible!")
    
                            
            
    def test_no_broken_links(self):
        print("\n\n\n\n")
        x=self.page.get_all_urls()
        if len(x)==0 :
            print("No link found :Test Passed!")
            assert True       
        else:
            for i in x:
                try:
                    response = rq.get(i)
                    status=response.status_code
                except:
                    status=600
                    
                temp = i+"  <---There is some essue with this link"   
                if check.is_true(status < 400,temp):
                    print(i+"  <---This link PASSED the test")
                               
            