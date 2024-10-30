import time
from selenium.webdriver.common.by import By
from page_objects.homePage import HomePage
from page_objects.checkoutPage import CheckOutPage
from page_objects.checkoutPage2 import CheckOutPage2
from page_objects.myaccountPage import MyAccountPage
from page_objects.loginPage import LoginPage
from page_objects.paymentsPage import PaymentsPage
from page_objects.signUpPage import SignupPage
from utilities.BaseClass import BaseClass



class TestSubmitOrder(BaseClass):

        def test_creditcard_payment(self,page_factory, user_data,cc_address,card_info):
            print("credit card payment scenario")
            homepage= page_factory["home"]
            homepage.signInButton()
            loginPage= page_factory["login"]
            loginPage.register_button()
            signupPage=page_factory["signup"]
            signupPage.fill_user_info(user_data)
            accountsPage=page_factory["accounts"]
            accountsPage.go_to_product_page()
            productsPage = page_factory["products"]
            productsPage.add_product_to_cart("Pliers")
            checkoutPage=productsPage.navigate_to_checkout()
            checkoutPage.check_out_button_1()
            checkout2Page=page_factory["checkout2"]
            checkout2Page.check_out_button_2()
            checkout2Page.enter_billing_address(cc_address)
            checkout2Page.proceed_to_checkout_3()
            paymentsPage=page_factory["payments"]
            paymentsPage.select_payment_option()
            paymentsPage.make_credit_card_payment(card_info)
            paymentsPage.check_payment_confirmation()

            time.sleep(4)






