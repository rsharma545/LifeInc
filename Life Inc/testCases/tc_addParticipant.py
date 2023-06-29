from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pageObject.lc_login_Page import Login
from testData.login_Data import LoginTestData
from utilities.utility import UtilityClass
from pageObject.lc_add_Participant import AddParticipant
from testData.addParticipant_Data import AddParticipantData
import time


class Tc05AddNewParticipant:

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
    lp.click(AddParticipant.locatorParticipants)
    time.sleep(4)
    lp.click(AddParticipant.locatorAddParticipant)
    time.sleep(4)
    lp.send_input_keys(AddParticipant.locatorPopupFirstName, AddParticipantData.first_name)
    time.sleep(2)
    lp.send_input_keys(AddParticipant.locatorPopupLastName, AddParticipantData.last_name)
    time.sleep(2)
    lp.click(AddParticipant.locatorPopupSelectSex)
    time.sleep(2)
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    time.sleep(2)
    lp.click(AddParticipant.locatorPopupNext)
    time.sleep(2)
    lp.send_input_keys(AddParticipant.locatorPopupMedicaid, AddParticipantData.medicaid)
    time.sleep(3)
    lp.click(AddParticipant.locatorPopupPrimaryDiagnosis)
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    time.sleep(3)
    lp.click(AddParticipant.locatorPopupYear)
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    time.sleep(2)
    lp.click(AddParticipant.locatorPopupSelectMonth)
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    time.sleep(2)
    lp.click(AddParticipant.locatorPopupSelectDay)
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    time.sleep(2)
    lp.click(AddParticipant.locatorPopupNext)
    time.sleep(2)
    lp.click(AddParticipant.locatorPopupProgram)
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    time.sleep(2)
    lp.click(AddParticipant.locatorAddParticipantTitle)
    time.sleep(2)
    lp.click(AddParticipant.locatorDevelopmentSpecialist)
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    time.sleep(2)
    #lp.click(AddParticipant.locatorPopupFinish)
    #time.sleep(4)


