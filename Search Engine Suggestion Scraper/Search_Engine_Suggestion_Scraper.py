from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.select import Select
import time
import pandas as pd

x=input("Enter a key word :")
print("Wait,It will take a while...\n")


try:
    ops=webdriver.ChromeOptions()
    ops.headless=True
    ops.add_argument("--headless=new")
    browser = webdriver.Chrome(options=ops)
    browser.implicitly_wait(10)
    
            


    try:
        browser.get('https://www.google.com')
        e1=browser.find_element(By.XPATH,"//textarea[@title='Search']")
        e1.send_keys(x)
        time.sleep(6)
        e1=browser.find_elements(By.XPATH,"//div[@role='presentation' and @class='wM6W7d']//span")
        a1=list()
        for i in e1:
            a1.append(i.text)
    except:
        print("> Failed to connect to google.\n")
    else:
        if(len(a1))>0:
            print("> Data have been successfully fetched from google.\n")
        else:
            print("> No data from google.\n")



    try:
        browser.get('https://duckduckgo.com')
        e2=browser.find_element(By.XPATH,"//input[@placeholder='Search without being tracked']")
        e2.send_keys(x)
        time.sleep(6)
        e2=browser.find_elements(By.XPATH,"//span[@class='searchbox_suggestionText__3x8nI']")
        a2=[]
        for i in e2:
            a2.append(i.text)
    except:
            print("> Failed to connect to duckduckgo.\n")
    else:
        if(len(a2))>0:
            print("> Data have been successfully fetched from duckduckgo.\n")
        else:
            print("> No data from duckduckgo.\n")



    try:
        browser.get('https://bing.com')
        e3=browser.find_element(By.XPATH,"//textarea[@type='search']")
        e3.send_keys(x)
        time.sleep(6)
        e3=browser.find_elements(By.XPATH,"//ul[@role='listbox']//li")
        a3=[]
        for i in e3:
            a3.append(i.text)
    except:
            print("> Failed to connect to bing.\n")
    else:
        if(len(a3))>0:
            print("> Data have been successfully fetched from bing.\n")
        else:
            print("> No data from bing.\n")



    try:
        browser.get('https://www.youtube.com')
        e4=browser.find_element(By.XPATH,"//input[@name='search_query']")
        e4.click()
        e4.send_keys(x)
        time.sleep(6)
        e4=browser.find_elements(By.XPATH,"//div[@role='option'  and   @aria-label]")
        a4=[]
        for i in e4:
            a4.append(i.get_attribute("aria-label"))
    except:
        print("> Failed to connect to youtube.\n")
    else:
        if(len(a4))>0:
            print("> Data have been successfully fetched from youtube.\n")
        else:
            print("> No data from youtube.\n")



    try:
        browser.get('https://www.ebay.com')
        print()
        e5=browser.find_element(By.XPATH,"//input[@title='Search']")
        e5.click()
        e5.send_keys(x)
        time.sleep(6)
        e5=browser.find_elements(By.XPATH,"//span[@class='ebay-autocomplete-suggestion']")
        a5=[]
        for i in e5:
            a5.append(i.text)
    except:
        print("> Failed to connect to ebay.\n")
    else:
        if(len(a5))>0:
            print("> Data have been successfully fetched from ebay.\n")
        else:
            print("> No data from ebay.\n")
            
            

        
    a=max(len(a1),len(a2),len(a3),len(a4),len(a5))
    while len(a1)<a:
        a1.append(None)

    while len(a2)<a:
        a2.append(None)

    while len(a3)<a:
        a3.append(None)

    while len(a4)<a:
        a4.append(None)

    while len(a5)<a:
        a5.append(None)


    d={'GOOGLE':a1,'DUCKDUCKGO':a2,'BING':a3,'YOUTUBE':a4,'EBAY':a5}
    df1=pd.DataFrame(d)
    df1.to_csv('report.csv')    
    print("Check Your Working Directory,Your Report Is Ready.\n")


except:
    print("Some Network ERROR Occur!\nCheck your internet connection & try again later.\n ")
finally:
    browser.quit()
