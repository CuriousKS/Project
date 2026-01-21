import time
from selenium import webdriver
from BasePage import ProjectGutenberg
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

#author="Rose Fyleman"
author=input("Enter the name of a author to download all his books from Project Gutenberg : ")

browser=webdriver.Chrome()
browser.implicitly_wait(8)

browser.get("https://www.gutenberg.org")
browser.maximize_window()


o1=ProjectGutenberg(browser)
o1.search(author)
books=o1.get_elements((By.XPATH,"//ul[@class='results']//li[@class='booklink']"))
i=0
n=len(books)

if(n==0):
    print("No result found!")
else:    
    while(i<n):
        books[i].click()
        o1.get_elements((By.XPATH,"//a[@title='Download' and @type='application/zip']"))[0].click()
        o1.search(author)
        books=o1.get_elements((By.XPATH,"//ul[@class='results']//li[@class='booklink']"))
        i=i+1
    
    print("Downloaded all books of author :",author,"successfully in .zip format.\n Number of books downloaded : ",i)
    
    
browser.quit()