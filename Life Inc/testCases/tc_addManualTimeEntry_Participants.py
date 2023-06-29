from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pageObject.lc_login_Page import Login
from testData.login_Data import LoginTestData
from utilities.utility import UtilityClass
from pageObject.lc_add_ManualTimeEntry_Participants import AddManualTEP
import time

class Tc11AddManualTEP:

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
    lp.click(AddManualTEP.locatorMenuParticipants)
    time.sleep(4)
    lp.click(AddManualTEP.locatorParticipant)
    time.sleep(2)
    lp.click(AddManualTEP.locatorTimeEntry)
    time.sleep(2)
    lp.click(AddManualTEP.locatorManualTimeEntry)
    time.sleep(2)
    lp.click(AddManualTEP.locatorAddEntryTime)
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    time.sleep(2)

    #lp.click(AddParticipant.locatorPopupFinish)
    #time.sleep(4)


