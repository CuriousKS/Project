# 📂 Postman Collections – Author API Testing

## 📖 Overview
This repository contains Postman collections created to test **Open Library Author APIs**.  
The collections include test cases for:
- Searching authors
- Fetching author details
- Fetching works by an author

The goal is to demonstrate **API testing skills** using Postman, including:
- Status code validation
- JSON structure checks
- Data-driven testing with multiple authors
- Negative test cases for error handling

---

## 🚀 How to Use

### 1. Import Collection
- Download the `.json` file from this repo (e.g., `Author.postman_collection.json`).
- Open Postman → **Collections** → **Import** → select the file.

### 2. Set Environment Variables
This collection uses the following variables:
- `BASE_URL` → e.g. `https://openlibrary.org`
- `authorName` → e.g. `H. C. Verma`
- `authorID` → e.g. `OL1115089A`
- `author.json` → used to validate JSON responses for author details

You can define these in **Postman Environments** or pass them via a **data file**.

### 3. Run Tests
- Open the **Collection Runner** in Postman.
- Upload the provided `authors.csv` or `authors.json` file to run tests for multiple authors.
- Postman will substitute `{{authorName}}` and `{{authorID}}` dynamically.
- View results in the runner or export them for reporting.

---

## 🧪 Example Test Cases
- **Status Code** → `pm.response.to.have.status(200)`
- **JSON Validation** → `pm.response.to.be.json`
- **Author Found** → `pm.expect(jsonData.numFound).to.be.at.least(1)`
- **Key Format** → `pm.expect(jsonData.key).to.eql("/authors/" + pm.variables.get("authorID"))`

---

## 📂 Repository Structure