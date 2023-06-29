from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pageObject.lc_login_Page import Login
from testData.login_Data import LoginTestData
from utilities.utility import UtilityClass
from pageObject.lc_add_ManualTimeEntry_Employee import AddManualTEE
from pageObject.lc_add_Employee import AddEmployee
import time

class Tc11AddManualTEE:

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
    lp.click(AddEmployee.locatorAdministration)
    time.sleep(2)
    lp.click(AddEmployee.locatorEmployees)
    time.sleep(4)
    lp.click(AddManualTEE.locatorEmployee)
    time.sleep(7)
    lp.click(AddManualTEE.locatorTimeEntries)
    time.sleep(2)
    lp.click(AddManualTEE.locatorManualTimeEntry)
    time.sleep(2)
    lp.click(AddManualTEE.locatorPopUpLocation)
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    time.sleep(3)
    lp.click(AddManualTEE.locatorPopUpSelectShiftType)
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    time.sleep(3)
    lp.click(AddManualTEE.locatorPopUpSelectProgram)
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    time.sleep(2)
    lp.click(AddManualTEE.locatorSelectTime)
    time.sleep(1)
    lp.click()

    #lp.click(AddParticipant.locatorPopupFinish)
    #time.sleep(4)


