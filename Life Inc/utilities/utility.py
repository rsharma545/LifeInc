import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from pageObject.lc_login_Page import Login


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

