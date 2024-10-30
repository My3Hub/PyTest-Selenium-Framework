import time
from selenium.webdriver.common.by import By
from page_objects.myaccountPage import MyAccountPage
from page_objects.signUpPage import SignupPage
from utilities.BaseClass import BaseClass


class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    registerlink = (By.XPATH, "//a[@data-test='register-link']")
    def register_button(self):
        self.driver.find_element(*LoginPage.registerlink).click()

    signin_with_google=(By.CSS_SELECTOR,".google-sign-in-button")
    def sign_in_with_google(self):
        return self.driver.find_element(*LoginPage.signin_with_google)

    submit_button = (By.CLASS_NAME, "btnSubmit")
    def login_page_submit(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def log_in(self,user_data):
        BaseClass.wait_for_the_visibility_of_element(self, LoginPage.signin_with_google)
        login_details = {
            "email": (By.ID, "email"),
            "password": (By.CSS_SELECTOR, "[placeholder*='password']")
        }
        for key,locator in login_details.items():
            element=self.driver.find_element(*locator)
            element.send_keys(user_data[key])

        BaseClass.wait_for_the_visibility_of_element(self,LoginPage.submit_button)
        LoginPage.login_page_submit(self).click()
        myAccountPage=MyAccountPage(self.driver)
        myAccountPage.user_account_displayed()
        return myAccountPage