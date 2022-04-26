from selenium import webdriver
import wegosty_locators as locators
from selenium.webdriver.chrome.service import Service
from time import sleep
import datetime
from selenium.webdriver.common.by import By


s = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'lanch {locators.app}')
    print('___________________________________________')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('http://34.233.225.85/students/admissions')
    if driver.current_url == 'http://34.233.225.85':
        print(f' WeGoStudy URL: {driver.current_url}')


def login():
    driver.find_element(By.XPATH, '//*[@id="toast-container"]').click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'LOGIN').click()
    sleep(1)
    driver.find_element(By.ID, 'user_email').send_keys('chris.velasco78@gmail.com')
    sleep(1)
    driver.find_element(By.ID, 'user_password').send_keys('123cctb')
    sleep(1)
    driver.find_element(By.XPATH, "//input[@value='SIGN IN']").click()
    # driver.find_element(By.NAME, 'commit').click()
    # driver.find_element(By.XPATH,'//*[@id="new_user"]/div[3]/input').click()


def log_out():
    sleep(8)
    driver.find_element(By.XPATH, '//div[@id="navbar-nav"]/ul[2]/li[2]/a/span').click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'Log out').click()


def tearDown():
    if driver is not None:
        print(f'_________________Test finished successfully at {datetime.datetime.now()}_________________')
        sleep(2)
        driver.close()
        driver.quit()


setUp()
login()
log_out()
tearDown()