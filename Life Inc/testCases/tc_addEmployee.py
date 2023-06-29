from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pageObject.lc_login_Page import Login
from testData.login_Data import LoginTestData
from utilities.utility import UtilityClass
from pageObject.lc_add_Employee import AddEmployee
from testData.addEmployee_Data import AddEmployeeData
import time


class Tc02AddNewEmployee:

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
    time.sleep(4)
    lp.click(AddEmployee.locatorEmployees)
    time.sleep(4)
    lp.click(AddEmployee.locatorAddEmployee)
    time.sleep(4)
    lp.send_input_keys(AddEmployee.locatorPopupName, AddEmployeeData.employee_name)
    time.sleep(2)
    lp.send_input_keys(AddEmployee.locatorPopupUsername, AddEmployeeData.employee_username)
    time.sleep(2)
    lp.send_input_keys(AddEmployee.locatorPopupPassword, AddEmployeeData.employee_password)
    time.sleep(2)
    lp.click(AddEmployee.locatorPopupNext)
    time.sleep(4)
    lp.click(AddEmployee.locatorProgram)
    time.sleep(3)
    action = ActionChains(driver)
    action.send_keys("administration").perform()
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    time.sleep(3)
    lp.click(AddEmployee.locatorProgramInfo)
    time.sleep(4)
    lp.click(AddEmployee.locatorRole)
    action = ActionChains(driver)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    time.sleep(3)
    lp.click(AddEmployee.locatorPopupNext)
    time.sleep(3)
    lp.send_input_keys(AddEmployee.locatorPopupEmail, 'test@life.com')
    lp.send_input_keys(AddEmployee.locatorPopupPhoneNumber, '0123456789')
    time.sleep(4)
    lp.click(AddEmployee.locatorPopupFinish)
    time.sleep(4)


