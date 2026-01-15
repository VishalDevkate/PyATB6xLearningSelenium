
---

# 🧪 Python Selenium 4.x – Web Automation Notes

Comprehensive notes and examples for **Web Automation using Selenium 4.x with Python**.
This repository serves as a practical reference for automation testers, QA engineers, and learners preparing for Selenium interviews or real-world automation projects.

---

## 📌 Overview

Selenium is an open-source framework used to automate web browsers.
These notes cover **Selenium 4.x**, its architecture, core concepts, best practices, and hands-on examples using **Python + PyTest**.

The content progresses from fundamentals to advanced topics like **XPath mastery, waits, actions, windows, iframes, grids, and Docker execution**.

---

## 🧠 Topics Covered

### 🔹 Selenium Fundamentals

* What is Selenium & History (RC → WebDriver → Selenium 4)
* Selenium vs Playwright vs Cypress
* When **NOT** to use Selenium
* WebDriver Architecture (Pre & Post Selenium 4 – W3C compliant)

### 🔹 Environment Setup

* IDEs: PyCharm, VS Code
* Browser Drivers (Chrome, Firefox, Edge, Safari)
* Virtual Environments (`virtualenv`)
* Logging with PyTest

### 🔹 Selenium WebDriver API

* WebDriver Hierarchy
* ChromeDriver & ChromeOptions
* Page Load Strategy
* Proxy Configuration
* Remote WebDriver (Local, Grid, Cloud)

### 🔹 Selenium Grid & Execution

* Grid 3 vs Grid 4 Architecture
* Grid Modes (Standalone, Hub-Node, Distributed)
* Running Grid using:

  * JAR
  * Docker
* Cloud Execution (BrowserStack)

### 🔹 Navigation & Browser Control

* `get()`, `back()`, `forward()`, `refresh()`
* Difference between `driver.close()` and `driver.quit()`

---

## 🔍 Locators & Element Identification

### Supported Locators

* ID, Name, Class Name
* Link Text / Partial Link Text
* CSS Selector
* XPath (Relative & Absolute)

### XPath Mastery

* XPath syntax & functions
* `contains()`, `starts-with()`, `text()`
* XPath Axes (ancestor, child, sibling, following)
* Best practices for writing efficient locators

### CSS Selectors

* Attribute selectors
* Pseudo-classes (`:first-child`, `:nth-child`)
* Advanced CSS strategies

---

## ⏳ Selenium Waits

* Implicit Wait
* Explicit Wait (Expected Conditions)
* Fluent Wait
* Best practices (Avoid `time.sleep()`)

---

## 🧩 Advanced Selenium Concepts

### 🔔 Alerts

* Accept, Dismiss, Get Text, Send Keys

### ☑️ Checkboxes & Radio Buttons

* Selection & validation

### 📊 Web Tables

* Static & Dynamic Tables
* Row/Column traversal
* Data extraction

### 🖱️ Actions Class

* Mouse actions (hover, drag-drop, right click)
* Keyboard actions (key down, key up, copy-paste)
* Scroll actions

### 🪟 Windows & Tabs

* Handling multiple windows
* Switching between parent & child windows

### 🖼️ IFrames

* Switch by ID, Name, Index, WebElement
* Real-world iframe automation examples

### 📂 File Upload

* Handling file upload inputs

### ⚙️ JavaScript Executor

* Click elements
* Scroll into view
* Modify DOM attributes

---

## 🧪 Assignments & Practice Scenarios

* Automate VWO Login (Valid & Invalid cases)
* Capture validation error messages
* Use Allure Reports
* Handle Heatmaps with Actions + Iframe + Window switching
* Real-world automation challenges

---

## 🛠️ Tech Stack

* **Language:** Python
* **Automation Tool:** Selenium 4.x
* **Test Framework:** PyTest
* **Reporting:** Allure
* **Execution:** Local, Grid, Docker, Cloud
* **Browser Support:** Chrome, Firefox, Edge

---

## 🎯 Who Should Use This Repo?

* Manual testers moving to automation
* Automation engineers using Selenium with Python
* QA professionals preparing for interviews
* Learners practicing real-world Selenium use cases

---

## 👤 Author

**Vishal Devkate**

---

## 📚 Credits & References

* The Testing Academy – Pramod Sir
* Selenium Official Documentation
* W3C WebDriver Specification
* BrowserStack
* SelectorsHub
* Guru99

---

## ⭐ Support

If you find this repository helpful:

* ⭐ Star the repo
* 🍴 Fork it
* 🧠 Use it to master Selenium Automation

---
