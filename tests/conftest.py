import pytest
from selenium import webdriver
import os

from page_objects.checkoutPage import CheckOutPage
from page_objects.checkoutPage2 import CheckOutPage2
from page_objects.homePage import HomePage
from page_objects.loginPage import LoginPage
from page_objects.myaccountPage import MyAccountPage
from page_objects.paymentsPage import PaymentsPage
from page_objects.productsPage import ProductsPage
from page_objects.signUpPage import SignupPage

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome", help="selected browser"
    )
# @pytest.fixture(scope="class")
# def driver(request):
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument("--incognito")
#     browser_name=request.config.getoption("browser_name")
#     if browser_name=='Chrome':
#         driver = webdriver.Chrome(chrome_options)
#     elif browser_name=='Edge':
#         driver=webdriver.Edge()
#
#     driver.get("https://practicesoftwaretesting.com/")
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     request.cls.driver=driver
#     yield
#     driver.close()

@pytest.fixture(scope="class")
def driver(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    browser_name = request.config.getoption("browser_name")

    if browser_name == 'Chrome':
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == 'Edge':
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get("https://practicesoftwaretesting.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def cc_address():
    return{
            "address": "6263 Yappon Dr",
            "city": "Your City",
            "state": "Your State",
            "country" : "US",
            "zip": "12345"
          }

@pytest.fixture(scope='class')
def user_data():
    return{
        "first_name": "mythri",
        "last_name": "ogoti",
        "date_of_birth": "12/02/1993",
        "address": "123 street",
        "city": "Test city",
        "state": "Texas",
        "zipcode": "12345",
        "country": "US",
        "phone_number": "1234567890",
        "email": "mythri5@gmail.com",
        "password": "Coco@0424"
    }

@pytest.fixture(scope='class')
def card_info():
    return{
    "card_number": "1234-1234-1234-1234",
    "expiration_date": "09/2029",
    "cvv": "123",
    "card_holder_name": "ABCDEFGH"
    }

@pytest.fixture(scope="class")
def page_factory(request, driver):
    driver = request.getfixturevalue("driver")

    return {
        "home": HomePage(driver),
        "login": LoginPage(driver),
        "signup": SignupPage(driver),
        "accounts":MyAccountPage(driver),
        "products":ProductsPage(driver),
        "checkout":CheckOutPage(driver),
        "checkout2":CheckOutPage2(driver),
        "payments":PaymentsPage(driver)
       }
