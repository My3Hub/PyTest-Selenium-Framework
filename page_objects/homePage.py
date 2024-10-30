from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self,driver):
       self.driver=driver
       self.signIn=(By.CSS_SELECTOR,"[data-test='nav-sign-in']")

    # signIn = (By.CSS_SELECTOR,"[data-test='nav-sign-in']")
    def signInButton(self):
        self.driver.find_element(*self.signIn).click()
