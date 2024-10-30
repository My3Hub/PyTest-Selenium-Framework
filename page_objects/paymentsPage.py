import time

from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass

class PaymentsPage:
    def __init__(self, driver):
        self.driver = driver

    payments_dropdown = (By.CSS_SELECTOR, "#payment-method")

    def payments_dropdown_menu(self):
        return self.driver.find_element(*PaymentsPage.payments_dropdown)

    def select_payment_option(self):
        BaseClass.select_by_value(self, self.payments_dropdown_menu(), "credit-card")

    confirm_button = (By.CSS_SELECTOR, "[data-test='finish']")

    def confirm_payment(self):
        self.driver.find_element(*PaymentsPage.confirm_button).click()

    def enter_card_details(self, card_info):
        Card_Details = {
            "card_number": (By.CSS_SELECTOR, "[id=credit_card_number]"),
            "expiration_date": (By.ID, "expiration_date"),
            "cvv": (By.CSS_SELECTOR, "#cvv"),
            "card_holder_name": (By.XPATH, "//input[@data-test='card_holder_name']")
        }
        for field, locator in Card_Details.items():
            element = self.driver.find_element(*locator)
            element.clear()
            element.send_keys(card_info[field])

    def make_credit_card_payment(self, card_info):
        self.enter_card_details(card_info)
        self.confirm_payment()

    order_id = (By.XPATH, "//div[@id='order-confirmation']/span")
    def order_Id(self):
        return self.driver.find_element(*PaymentsPage.order_id)

    confirmation_message = (By.CSS_SELECTOR, ".alert-success")
    def confirm_message(self):
        return self.driver.find_element(*PaymentsPage.confirmation_message)
    def check_payment_confirmation(self):
        BaseClass.wait_for_the_visibility_of_element(self,PaymentsPage.confirmation_message)

        if PaymentsPage.confirm_message(self).is_displayed():
            print("Order is placed")
            PaymentsPage.confirm_payment(self)
            # time.sleep(4)
            BaseClass.wait_for_the_visibility_of_element(self, PaymentsPage.order_id)
            order_id_element = PaymentsPage.order_Id(self)  # Use self here
            print("Order ID:", order_id_element.text)
        else:
            print("Payment failed")


