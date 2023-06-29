from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pageObject.lc_login_Page import Login
from testData.login_Data import LoginTestData
from utilities.utility import UtilityClass
from pageObject.lc_download_X12_CSR import DownloadX12CSR
import time


class Tc10ApproveCSR:

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
    lp.click(DownloadX12CSR.locatorMenuApprovals)
    time.sleep(2)
    lp.click(DownloadX12CSR.locatorAllApprovals)
    time.sleep(3)
    lp.click(DownloadX12CSR.locatorWaitingForSubmission)
    time.sleep(2)
    lp.click(DownloadX12CSR.locatorVerticalBtn)
    time.sleep(2)
    #lp.click(DownloadX12CSR.locatorDownloadX12)
    #time.sleep(4)
