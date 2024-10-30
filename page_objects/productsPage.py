import time
from selenium.webdriver.common.by import By
from page_objects.checkoutPage import CheckOutPage
from utilities.BaseClass import BaseClass

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    products = (By.CSS_SELECTOR, "h5[data-test='product-name']")
    add_to_cart = (By.XPATH, "//button[@id='btn-add-to-cart']")
    card_update = (By.XPATH, "//div[@aria-label='Product added to shopping cart.']")
    cart_icon = (By.CSS_SELECTOR, "a[aria-label='cart']")

    def product_list(self):
        BaseClass.wait_for_the_visibility_of_elements(self, self.products)
        return self.driver.find_elements(*self.products)

    def add_product_to_cart(self, product_name="Pliers"):
        for product in self.product_list():
            if product.text == product_name:
                product.click()  # Select the product
                self.driver.find_element(*self.add_to_cart).click()  # Add to cart
                break

        BaseClass.wait_for_the_visibility_of_element(self, self.card_update)
        BaseClass.wait_for_the_invisibility_of_elements(self, self.card_update)

    def navigate_to_checkout(self):
        self.driver.find_element(*self.cart_icon).click()
        return CheckOutPage(self.driver)

    # def add_product_and_checkout(self, product_name="Pliers"):
    #     self.add_product_to_cart(product_name)
    #     return self.navigate_to_checkout()
