from selenium import webdriver
import time
import unittest
from POM.Loginpage import loginpage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path= "C:/Users/user/Downloads/geckodriver-v0.33.0-win64/geckodriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_Login_valid(self):
        driver = self.driver

        driver.get("https://dev2.hypeddit.com/devlock")
        time.sleep(2)

        login = loginpage(driver)
        login.enter_password_dev("BetterDevTest8675!")
        login.click_submit()

        #time.sleep(2)

        login.click_login_dev()
        login.enter_username("harry@baltech.in")
        login.enter_password("123456")
        login.click_login()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Task completed")




