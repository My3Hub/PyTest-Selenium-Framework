import time
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class CheckOutPage2:

    def __init__(self,driver):
        self.driver=driver

    checkout_2=(By.CSS_SELECTOR,"[data-test='proceed-2']")
    def check_out_button_2(self):
        BaseClass.wait_for_the_visibility_of_element(self,CheckOutPage2.checkout_2)
        return self.driver.find_element(*CheckOutPage2.checkout_2).click()


    def enter_billing_address(self,cc_address):
        billing_address = {
            "address": (By.CSS_SELECTOR, "[formcontrolname='address']"),
            "city": (By.CSS_SELECTOR, "#city"),
            "state": (By.CSS_SELECTOR, "input[placeholder='State *']"),
            "country": (By.ID, "country"),
            "zip": (By.XPATH, "//input[@formcontrolname='postcode']"),
        }
        for field,value in billing_address.items() :
            element=self.driver.find_element(*value)
            element.clear()
            element.send_keys(cc_address[field])

    checkout_3 = (By.CSS_SELECTOR,"[data-test='proceed-3']")
    def proceed_to_checkout_3(self):
        BaseClass.wait_for_the_visibility_of_element(self,CheckOutPage2.checkout_3)
        self.driver.find_element(*CheckOutPage2.checkout_3).click()









