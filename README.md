# Automating E-Commerce Website Scenarios using PyTest Framework
Website Used:[practice software testing](https://practicesoftwaretesting.com)
This framework is designed to test end-to-end (E2E) scenarios for the specified e-commerce site. It was developed using PyTest-Selenium with a page object model approach.
## Table of contents
- Overview
* Technologies Used
+ Framework Structure
- Test Case Example
* Reporting
+ Installation

### Overview
This automation framework is designed to test various user scenarios on the specified e-commerce website. The framework is modular and scalable, making it easy to add new test cases and functionalities.

### Technologies Used
1. Python for scripting
2. Selenium for web automation
3. PyTest for test case management
4. Page Object Model for organizing code
5. HTML Reporting for visual test results (coming soon!)
   
### Framework Structure
#fffff **page_objects**/: Contains page object classes for different pages (e.g., HomePage, CheckoutPage, LoginPage, etc.)
tests/: Contains test case files that utilize the page objects.
utilities/: Contains utility classes (e.g., BaseClass) for shared functions.
data/: Directory for storing test data in dictionary format.
Test Case Example
Test Case: test_creditcard_payment
Description:
Simulates the process of registering a user, adding a product to the cart, and completing the checkout using a credit card.

Key Steps:

Sign in and register a new user.
Navigate to the product page and add a product to the cart.
Complete the checkout process, entering billing information and selecting credit card payment.
Verify payment confirmation.
