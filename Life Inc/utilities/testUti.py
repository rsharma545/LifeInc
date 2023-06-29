import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver


class UtilityClass:

    def __init__(self, driver):
        self.driver = driver

    def send_input_keys(self, locator, inputKeys):
        self.driver.find_element(By.XPATH, locator).send_keys(inputKeys)

    def click(self, locator):
        self.driver.find_element(By.XPATH, locator).click()

    def elastic_search_dd(self):
        action = ActionChains(self.driver)
        action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
        action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    def type_in_field(self, locator, value):
        val = value
        for i in range(0, len(val)):
            elem = val[i]
            self.send_input_keys(locator, elem)
            time.sleep(2)

    def validate_element(self, locator):
        check_elem = self.driver.find_element(By.XPATH, locator).is_displayed()
        return bool(check_elem)

    def validate_data(self, locator, value):

        menu = self.driver.find_elements(By.XPATH, locator)
        for x in range(len(menu)):
            print(menu[x].text)
            listValue = menu[x].text
            if listValue == value:
                return True
            else:
                return False

    def get_input_value(self, locator):
        inputValue = self.driver.find_element(By.XPATH, locator).get_attribute('value')
        return inputValue

    def wait_for_element(self, locator):
        elemWait = WebDriverWait(self.driver, 10)
        elemWait.until(EC.presence_of_element_located((By.XPATH, locator)))





