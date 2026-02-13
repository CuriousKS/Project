import pytest
import pytest_check as check
from selenium import webdriver
from BasePage import ProjectGutenberg
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import requests as rq

class TestLogin:
    @pytest.fixture(params=["chrome","firefox"],scope="function",autouse=True) 
    def setup_and_teardown(self,request):
        if request.param=="chrome":
            self.driver = webdriver.Chrome()
            
        if request.param=="firefox":
            self.driver = webdriver.Firefox()

        if request.param=="edge":
            self.driver = webdriver.Edge()

        self.driver.maximize_window()
        self.driver.get("https://www.gutenberg.org")
        self.page=ProjectGutenberg(self.driver)
        yield
        self.driver.quit()


    def test_book_download(self):
        print("\n\n\n\n")
        self.page.search("The Roman hat mystery by Ellery Queen")
        print(self.page.get_title())
        assert "The Roman hat mystery by Ellery Queen" in  self.page.get_title() ,"ERROR in test_search_bar while downloading a book"
        download_url=self.driver.find_element(By.XPATH,"//a[@accesskey='1']").get_attribute('href')
        response=rq.get(download_url)
        assert response.status_code==200,"DOWNLOAD FAILED!"
        assert len(response.content)>0,"DOWNLOAD FILE IS EMPTY!"
        print(len(response.content))
        
       
    def test_visibility_of_common_elements(self):
        print("\n\n\n\n")
        d1=self.page.__dict__
        for i in d1:
            if i=='driver':
                continue
            
            if check.is_true(self.page.get_common_element(i) != None ,i+" not found!") :
                    print(i,"<-----This element is visible")
                    if check.is_true(self.page.get_common_element(i).is_enabled() != False ,i+" not enabled!"):
                        print("\t",i,"<-----This element is enable")
                    else:
                       print("\t",i,"<-----THIS ELEMENT IS NOT ENABLE")
                   
            else:
                print(i,"<-----THIS ELEMENT IS NOT VISIBLE!")
                                    
    
                            
   
    def test_no_broken_links(self,request):
        print("\n\n\n\n")
        x=self.page.get_all_urls()
        if len(x)==0 :
            print("No link found :Test Passed")
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
                    
    
    
                    
                               
            