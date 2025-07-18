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

🔁 Regression Testing<br>
    This project includes regression-style test cases designed to ensure that core functionality remains stable after updates or code changes.<br><br><br>
    This test suite performs:<br>
        - Visibility checks for critical UI elements across the homepage<br>
        - Search bar validation to confirm consistent input response<br>
        - Broken link detection<br>
<br>
✅ All 3 tests passed successfully!<br>
    Terminal Output Snapshot:<br>
        BaseTestScreenschot1.png<br>
        BaseTestScreenschot2.png<br>
        BaseTestScreenschot3.png<br>
        BaseTestScreenschot4.png<br>   
---------------------------------------------------------------------------------------------------------------------------------------------
## 📂 Folder Structure

PageObjectModel 
│
├── BasePage.py                     # Page Object model for homepage locators and actions<br> 
├── BaseTest.py                     # Contains Pytest-based UI test functions<br> 
├── pg_bot.py                       # Script to auto-download .zip books by specified author<br> 
├── README.md                       # This file<br> 
└── requirements.txt                # Optional dependency list<br>
<br>
├── BaseTestScreenschot1.png        #Terminal output snapschots of:  pytest -rA -v BaseTest.py<br>
├── BaseTestScreenschot2.png        #Terminal output snapschots of:  pytest -rA -v BaseTest.py<br>    
├── BaseTestScreenschot3.png        #Terminal output snapschots of:  pytest -rA -v BaseTest.py<br>
└── BaseTestScreenschot4.png        #Terminal output snapschots of:  pytest -rA -v BaseTest.py<br>





