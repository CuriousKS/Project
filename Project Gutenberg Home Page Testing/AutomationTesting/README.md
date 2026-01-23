# 📚 Project Gutenberg Automation Suite

This repository contains a Python based automation suite built with Selenium WebDriver, 
structured using the Page Object Model (POM) design pattern, and tested with Pytest.

ChromeDriver Setup Instructions : This project assumes chromedriver is available in your system PATH.
FirefoxDriver Setup Instructions : This project assumes geckodriver is available in your system PATH.


The project targets the publicly accessible website [Project Gutenberg](https://www.gutenberg.org), 
a digital library of free eBooks.

---------------------------------------------------------------------

## 🚀 Features

- ✅ Home page interaction via POM structure
- ✅ Search functionality test and title verification
- ✅ Detection of broken links (HTTP status ≥ 400)
- ✅ Download automation of all .zip book formats by author name
- ✅ Scalable object repository and modular design
- ✅ Generate HTML Report

--------------------------------------------------------------------------------------------------------------------------------------------
## 🔍 Base Test – Overview

🔁 Regression Testing<br>
    This project includes regression-style test cases designed to ensure that core functionality remains stable after updates or code changes.<br><br><br>
    This test suite performs:<br>
        - Visibility checks for critical UI elements across the homepage<br>
        - Book download through search bar<br>
        - Broken link detection<br>
<br>



✅   Terminal Output Snapshot:<br>
        Screenschot1.png<br>
        Screenschot2.png<br>
        Screenschot3.png<br>
        Screenschot4.png<br>
        Screenschot5.png<br>
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

├── Screenschot1.png                 #Terminal output snapschots of:  pytest -rA -v BaseTest.py --html=report.html
├── Screenschot2.png                 #Terminal output snapschots of:  pytest -rA -v BaseTest.py --html=report.html   
├── Screenschot3.png                 #Terminal output snapschots of:  pytest -rA -v BaseTest.py --html=report.html
├── Screenschot4.png                 #Terminal output snapschots of:  pytest -rA -v BaseTest.py --html=report.html
└── Screenschot5.png                 #Terminal output snapschots of:  pytest -rA -v BaseTest.py --html=report.html

```




