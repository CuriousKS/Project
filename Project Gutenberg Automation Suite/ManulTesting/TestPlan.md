📄 Test Plan – Project Gutenberg Homepage Testing

__1. Introduction__
This Test Plan defines the overall strategy for testing the Project Gutenberg homepage.
It combines manual and automation testing to validate critical functionalities such as the search bar,
navigation buttons, donate button, book image redirections, and broken link checks.


__2. Objectives__
- Ensure functional correctness of homepage features.  
- Validate usability and redirection accuracy.  
- Automate repetitive tasks (link validation, book download).  
- Provide complete coverage through manual exploratory testing and automated regression.


__3. Scope of Testing__
In Scope
- Search bar functionality (valid, invalid, empty, special characters).  
- Header and footer navigation buttons.  
- Donate button redirection.  
- Book image redirections (Newest Releases, Most Popular).  
- Broken link validation via automation.  


__Out of Scope__
- External site content (social media platforms, book text).  
- Cosmetic UI details (fonts, hover effects).  
- Backend database queries not exposed to UI.


__4. Test Approach__
Manual Testing
- Positive, negative, and boundary test cases.  
- Exploratory testing for usability.  
- Cross-browser validation (Chrome, Firefox, Edge, Safari).  


Automation Testing
- Selenium script to:  
- Validate search bar functionality.  
- Verify existence of header/footer buttons.  
- Check for broken links.  
- Download a book using search.  
- Automation results documented in automation_report.md.


__5. Entry Criteria__  
- Test cases prepared and reviewed.  
- Test environment setup complete.  
- Automation script ready.  

__6. Exit Criteria__
- All manual test cases executed.  
- Automation script executed successfully.  
- All critical defects resolved or deferred with approval.  
- Test summary report prepared.  


__7. Deliverables__
- Manual: SRS.md, TestPlan.md, TestCases.xlsx, TestSummaryReport.md, BugReportTemplate.md.  
- Automation: gutenbergtest.py, requirements.txt, automationreport.md.  

__8. Environment__
- Browsers: Chrome , Firefox, Edge  
- OS: Windows 11  
- Tools: Selenium, Python, Excel.  


__9. Schedule__
- Requirement Analysis: 1/2 day 
- Test Planning: 1/2 day  
- Test Case Design: 1/2 day  
- Environment Setup: 1/2 day 
- Test Execution (Manual): 1/2 day  
- Test Execution (Automation): 1/2 days  
- Test Closure: 1/2 day   


__10. Risks & Mitigation__
- Risk: Large number of links → Mitigation: Automate link validation.  
- Risk: Browser compatibility issues → Mitigation: Perform cross-browser testing.  
- Risk: External site downtime → Mitigation: Validate only redirection, not external content.  

