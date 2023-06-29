from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pageObject.lc_login_Page import Login
from testData.login_Data import LoginTestData
from utilities.utility import UtilityClass
from pageObject.lc_add_ManualUnitsEntryCSR import ManualUnitsEntryCSR
import time


class Tc08ManualUnitsEntryCSR:

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
    lp.click(ManualUnitsEntryCSR.locatorMenuParticipants)
    time.sleep(4)
    lp.click(ManualUnitsEntryCSR.locatorParticipant)
    time.sleep(10)
    lp.click(ManualUnitsEntryCSR.locatorCSRs)
    time.sleep(3)
    lp.click(ManualUnitsEntryCSR.locatorViewIcon)
    time.sleep(2)
    lp.click(ManualUnitsEntryCSR.locatorManualEntry)
    time.sleep(2)
    lp.click(ManualUnitsEntryCSR.locatorServiceCode)
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    time.sleep(3)
    lp.send_input_keys(ManualUnitsEntryCSR.locatorSun, '1')
    lp.send_input_keys(ManualUnitsEntryCSR.locatorMon, '1')
    lp.send_input_keys(ManualUnitsEntryCSR.locatorTue, '1')
    lp.send_input_keys(ManualUnitsEntryCSR.locatorWed, '1')
    lp.send_input_keys(ManualUnitsEntryCSR.locatorThr, '1')
    lp.send_input_keys(ManualUnitsEntryCSR.locatorFri, '1')
    lp.send_input_keys(ManualUnitsEntryCSR.locatorSat, '1')
    time.sleep(2)
    #lp.click(ManualUnitsEntryCSR.locatorAddEntry)
    time.sleep(2)
