import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("driver")
class BaseClass:

    def select_by_value(self,element,value):
        dropdown_value=Select(element)
        dropdown_value.select_by_value(value)

    def wait_for_the_visibility_of_element(self,locator):
        wait=WebDriverWait(self.driver,10)
        wait.until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_the_visibility_of_elements(self,list_values):
        wait=WebDriverWait(self.driver,10)
        wait.until(expected_conditions.presence_of_all_elements_located(list_values))

    def wait_for_the_invisibility_of_elements(self,locator):
        wait=WebDriverWait(self.driver,10)
        wait.until(expected_conditions.invisibility_of_element_located(locator))

    def wait_for_the_element_to_be(self,element):
        wait=WebDriverWait(self.driver,10)
        wait.until(expected_conditions.element_to_be_clickable(element))
