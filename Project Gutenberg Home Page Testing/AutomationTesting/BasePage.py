from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProjectGutenberg:
    def __init__(self,driver):
        self.driver=driver
        self.about1=(By.XPATH,"//label[@class='dropdown-button']")
        self.frequently_downloaded1=(By.XPATH,"/html/body/div[1]/header/div[3]/div[2]/a[1]")
        self.main_categories1=(By.PARTIAL_LINK_TEXT,"Main Categories")
        self.reading_lists1=(By.XPATH,"//a[@class='link-reading-lists']")
        self.search_options1=(By.XPATH,"//a[@class='link-advanced-search']")
        self.search_bar1=(By.XPATH,"//input[@class='search-input']")
        self.go_button1=(By.XPATH,"//button[@class='search-button']")#
        self.paypal1=(By.XPATH,"//input[@class='donbtn']")
        self.donate1=(By.XPATH,"//a[@class='donate-link']")
        self.icon1=(By.XPATH,"//img[@alt='Project Gutenberg']")        
#        self.FacebookIcon2=(By.XPATH,"//img[@alt='Facebook icon']") #<--2 web elements
#        self.MastodonIcon2=(By.XPATH,"//img[@alt='Mastodon icon']") #<--2 web elements
#        self.BlueskyIcon2=(By.XPATH,"//img[@alt='Bluesky icon']")   #<--2 web elements       
#        self.nfone2=(By.XPATH,"//li[normalize-space(text())='News feeds of new eBooks:']")  #<--news feed of new ebooks        
        self.apg2=(By.XPATH,"//div[@class='footer']//a[@href='/about/']")   #<--About Project Gutenberg        
        self.PrivacyPolicy2=(By.XPATH,"//a[normalize-space(text()) = 'Privacy policy']")
        self.Permissions2=(By.XPATH,"//a[normalize-space(text()) = 'Permissions']")
        self.Terms_of_use2=(By.XPATH,"//a[normalize-space(text()) = 'Terms of Use']")
        self.ContactUs2=(By.XPATH,"//div[@class='footer']//a[@href='/about/contact_information.html']")
        self.Help2=(By.XPATH,"//a[normalize-space(text())='Help']")
        
        
        
    def get_common_element(self,x):
        temp=getattr(self,x)
        try:
            temp1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(temp))
            return temp1 
        except :#TimeoutError:
            return None
            

    def get_elements(self,x):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(x))
        except:
            return []

        
        
    def search(self,book_name):
        self.get_common_element("search_bar1").send_keys(book_name)
        self.get_common_element("go_button1").click()
        
    def get_title(self):
        return self.driver.title
        
       
    def get_all_urls(self):
        x= self.get_elements((By.XPATH,"//*[@href]"))
        index=0
        for i in x:
            i=i.get_attribute('href')
            if not('http' in i):
                x[index]="https://www.gutenberg.org"+i
            else:
                x[index]=i 
            index=index+1
        return x 
              

        
        
        
        
        
        
        
        
        
        
        
                