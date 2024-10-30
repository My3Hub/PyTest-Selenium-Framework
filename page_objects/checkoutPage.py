from selenium.webdriver.common.by import By

from page_objects.checkoutPage2 import CheckOutPage2
from utilities.BaseClass import BaseClass


class CheckOutPage:

    def __init__(self,driver):
        self.driver=driver

    checkout_1=(By.CSS_SELECTOR,"[data-test='proceed-1']")
    def check_out_button_1(self):
        BaseClass.wait_for_the_visibility_of_element(self,CheckOutPage.checkout_1)
        self.driver.find_element(*CheckOutPage.checkout_1).click()






