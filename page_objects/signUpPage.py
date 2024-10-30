import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from page_objects.homePage import HomePage


class SignupPage:
    def __init__(self, driver):
        self.driver = driver

    submit = (By.CSS_SELECTOR, "[type=submit]")

    def submit_button(self):
        self.driver.find_element(*SignupPage.submit).click()

    User_Details = {
        "first_name": (By.ID, "first_name"),
        "last_name": (By.ID, "last_name"),
        "date_of_birth": (By.ID, "dob"),
        "address": (By.ID, "address"),
        "zipcode": (By.CSS_SELECTOR, "[data-test='postcode']"),
        "city": (By.ID, "city"),
        "state": (By.ID, "state"),
        "country": (By.ID, "country"),
        "phone_number": (By.ID, "phone"),
        "email": (By.ID, "email"),
        "password": (By.CSS_SELECTOR, "[type='password']")
    }

    email_exists = (By.CSS_SELECTOR, ".help-block")

    def email_used(self):
        return self.driver.find_element(*SignupPage.email_exists)

    def fill_user_info(self, user_data):
        for field, value in user_data.items():
            details = self.driver.find_element(*SignupPage.User_Details[field])
            if isinstance(details, Select):
                select = Select(details)
                select.select_by_value(value)
            else:
                details.send_keys(value)

        self.submit_button()

        # Check if the email is already in use
        if self.when_email_exists():
            self.handle_email_exists(user_data)
        else:
            self.login_user(user_data)

    def when_email_exists(self):
        try:
            return self.email_used().is_displayed()
        except Exception as e:
            print(f"Error checking email existence: {e}")
            return False  # Assume email does not exist if check fails

    def handle_email_exists(self, user_data):
        print("Email already exists. Navigating to login.")
        homePage = HomePage(self.driver)
        homePage.signInButton()
        self.login_user(user_data)

    def login_user(self, user_data):
        from page_objects.loginPage import LoginPage
        loginPage = LoginPage(self.driver)  # Initialize the LoginPage
        loginPage.log_in(user_data)  # Log in with user data
