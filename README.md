# 📚 Project Gutenberg Automation Suite

This repository contains a Python-based automation suite built with Selenium WebDriver, 
structured using the Page Object Model (POM) design pattern, and tested with Pytest.

ChromeDriver Setup Instructions : This project assumes chromedriver is available in your system PATH.

The project targets the publicly accessible website [Project Gutenberg](https://www.gutenberg.org), 
a digital library of free eBooks.

---------------------------------------------------------------------

## 🚀 Features

- ✅ Home page interaction via POM structure
- ✅ Search functionality test and title verification
- ✅ Detection of broken links (HTTP status ≥ 400)
- ✅ Download automation of all .zip book formats by author name
- ✅ Scalable object repository and modular design

--------------------------------------------------------------------------------------------------------------------------------------------
## 🔍 Base Page Test – Overview

    🔁 Regression Testing
    This project includes regression-style test cases designed to ensure that core functionality remains stable after updates or code changes.

    This test suite performs:
        - Visibility checks for critical UI elements across the homepage
        - Search bar validation to confirm consistent input response
        - Broken link detection

    ✅ All 3 tests passed successfully!
    Terminal Output Snapshot:
        BaseTestScreenschot1.png
        BaseTestScreenschot2.png
        BaseTestScreenschot3.png
        BaseTestScreenschot4.png
       
---------------------------------------------------------------------------------------------------------------------------------------------
## 📂 Folder Structure
```
PageObjectModel 
│
├── BasePage.py                     # Page Object model for homepage locators and actions 
├── BaseTest.py                     # Contains Pytest-based UI test functions 
├── pg_bot.py                       # Script to auto-download .zip books by specified author 
├── README.md                       # This file 
└── requirements.txt                # Optional dependency list

├── BaseTestScreenschot1.png        #Terminal output snapschots of:  pytest -rA -v BaseTest.py
├── BaseTestScreenschot2.png        #Terminal output snapschots of:  pytest -rA -v BaseTest.py      
├── BaseTestScreenschot3.png        #Terminal output snapschots of:  pytest -rA -v BaseTest.py
└── BaseTestScreenschot4.png        #Terminal output snapschots of:  pytest -rA -v BaseTest.py
```




