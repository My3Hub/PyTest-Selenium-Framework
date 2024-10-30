import time
from selenium.webdriver.common.by import By

from page_objects.productsPage import ProductsPage
from utilities.BaseClass import BaseClass

class MyAccountPage:

    def __init__(self,driver):
        self.driver=driver

    categories = (By.CSS_SELECTOR,"[data-test='nav-categories']")
    def categories_button(self):
        return self.driver.find_element(*MyAccountPage.categories)

    hand_tools=(By.CSS_SELECTOR,"[data-test='nav-hand-tools']")
    def product_hand_tools(self):
        return self.driver.find_element(*MyAccountPage.hand_tools)

    def go_to_product_page(self):
        MyAccountPage.categories_button(self).click()
        # time.sleep(2)
        BaseClass.wait_for_the_visibility_of_element(self,MyAccountPage.hand_tools)
        # time.sleep(2)
        MyAccountPage.product_hand_tools(self).click()
        productsPage=ProductsPage(self.driver)
        return productsPage

    myaccount_Menu=(By.CSS_SELECTOR,"[id='menu']")
    def my_account_menu(self):
        return self.driver.find_element(*MyAccountPage.myaccount_Menu)

    def user_account_displayed(self):
        # time.sleep(2)
        BaseClass.wait_for_the_visibility_of_element(self,MyAccountPage.myaccount_Menu)


