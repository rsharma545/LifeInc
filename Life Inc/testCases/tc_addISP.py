from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pageObject.lc_login_Page import Login
from testData.login_Data import LoginTestData
from utilities.utility import UtilityClass
from pageObject.lc_add_ISP import AddISP
from testData.addParticipant_Data import AddParticipantData
import time


class Tc06AddISP:

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
    time.sleep(3)
    lp.click(AddISP.locatorMenuParticipants)
    time.sleep(3)
    lp.click(AddISP.locatorParticipant)
    time.sleep(4)
    lp.click(AddISP.locatorISP)
    time.sleep(2)
    lp.click(AddISP.locatorAddISP)
    time.sleep(2)
    lp.click(AddISP.locatorCalendar)
    time.sleep(4)
    lp.click(AddISP.locatorThisMonth)
    time.sleep(4)
    lp.click(AddISP.locatorSave)
    time.sleep(2)
    lp.click(AddISP.locatorSelectService)
    time.sleep(2)
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    time.sleep(3)
    lp.send_input_keys(AddISP.locatorAuthorizationNumber, '12345')
    time.sleep(2)
    lp.send_input_keys(AddISP.locatorWeeklyMaxUnits, '12')
    time.sleep(2)
    lp.click(AddISP.locatorSave)
    time.sleep(3)

