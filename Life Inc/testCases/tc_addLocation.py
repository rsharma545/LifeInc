from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pageObject.lc_login_Page import Login
from testData.login_Data import LoginTestData
from utilities.utility import UtilityClass
from pageObject.lc_add_Location import AddLocation
from testData.addLocation_Data import AddLocationData
import time


class Tc04AddNewLocation:

    option = Options()
    option.add_argument("--disable-notifications")
    driver = webdriver.Chrome(chrome_options=option, executable_path=ChromeDriverManager().install())
    loginTD = LoginTestData
    driver.get(loginTD.baseURL)
    driver.maximize_window()
    time.sleep(5)
    lp = UtilityClass(driver)
    lp.send_input_keys(Login.locatorUsername, loginTD.username)
    lp.send_input_keys(Login.locatorPassword, loginTD.password)
    lp.click(Login.locatorLoginBtn)
    time.sleep(4)
    lp.click(AddLocation.locatorSettings)
    time.sleep(5)
    lp.click(AddLocation.locatorLocations)
    time.sleep(7)
    lp.click(AddLocation.locatorAddLocation)
    time.sleep(3)
    lp.send_input_keys(AddLocation.locatorLocationName, AddLocationData.location_name)
    time.sleep(2)
    lp.send_input_keys(AddLocation.locatorAddressLine1, AddLocationData.address_line_1)
    time.sleep(2)
    lp.send_input_keys(AddLocation.locatorCity, AddLocationData.city)
    time.sleep(2)
    lp.send_input_keys(AddLocation.locatorState, AddLocationData.state)
    time.sleep(2)
    lp.send_input_keys(AddLocation.locatorZip, AddLocationData.zip)
    time.sleep(2)
    lp.click(AddLocation.locatorLocationType)
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    time.sleep(3)
    #lp.click(AddLocation.locatorCreate)
    time.sleep(4)


