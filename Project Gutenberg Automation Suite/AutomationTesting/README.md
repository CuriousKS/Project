# 📚 Project Gutenberg Automation Suite

This repository contains a Python based automation suite built with Selenium WebDriver, 
structured using the Page Object Model (POM) design pattern, and tested with Pytest.

ChromeDriver Setup Instructions : This project assumes chromedriver is available in your system PATH.<br>
FirefoxDriver Setup Instructions : This project assumes geckodriver is available in your system PATH.

The project targets the publicly accessible website [Project Gutenberg](https://www.gutenberg.org), 
a digital library of free eBooks.

---------------------------------------------------------------------

## 🚀 Features

- ✅ Home page interaction via POM structure
- ✅ Search bar functionality test
- ✅ Validate book download using search bar  
- ✅ Verify availability of headers and footers buttons
- ✅ Detection of broken links (HTTP status code ≥ 400)
- ✅ Generate HTML Report

--------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------
## 📂 Folder Structure
```
PageObjectModel 
│
├── BasePage.py                     # Page Object model for homepage locators and actions
├── BaseTest.py                     # Contains Pytest-based UI test functions
├── pg_bot.py                       # Script to auto-download .zip books by specified author 
├── README.md                       # This file
└── requirements.txt                # Other dependency list

├── Screenschot1.png                 #Terminal output screenschot of:  pytest -rA -v BaseTest.py --html=report.html
├── Screenschot2.png                 #Terminal output screenschot of:  pytest -rA -v BaseTest.py --html=report.html   
├── Screenschot3.png                 #Terminal output screenschot of:  pytest -rA -v BaseTest.py --html=report.html
├── Screenschot4.png                 #Terminal output screenschot of:  pytest -rA -v BaseTest.py --html=report.html
└── Screenschot5.png                 #Terminal output screenschot of:  pytest -rA -v BaseTest.py --html=report.html
```





