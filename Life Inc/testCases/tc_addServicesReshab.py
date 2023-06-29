from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pageObject.lc_login_Page import Login
from testData.login_Data import LoginTestData
from utilities.utility import UtilityClass
from pageObject.lc_add_ServiceReshab import NewServices
from testData.addServices_Data import NewServicesData
import time


class Tc03AddNewService:

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
    lp.click(NewServices.locatorSettings)
    time.sleep(5)
    lp.click(NewServices.locatorServices)
    time.sleep(7)
    lp.click(NewServices.locatorAddService)
    time.sleep(2)
    lp.click(NewServices.locatorProgram)
    time.sleep(3)
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    time.sleep(3)
    lp.send_input_keys(NewServices.locatorServicesCode, NewServicesData.service_code)
    time.sleep(3)
    lp.click(NewServices.locatorUnit)
    time.sleep(3)
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    lp.send_input_keys(NewServices.locatorUnitPrice, NewServicesData.unit_price)
    time.sleep(4)
    #lp.click(NewServices.locatorPopupAddServices)
    time.sleep(4)


