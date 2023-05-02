from selenium import webdriver
import time
import os

chromedriver = "C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()

driver.get("https://dev2.hypeddit.com/devlock")
driver.find_element("xpath", "//input[@placeholder='Password']").send_keys("BetterDevTest8675!")
driver.find_element("xpath", "//button[normalize-space()='SUBMIT']").click()

time.sleep(7)

driver.find_element("xpath", "//a[normalize-space()='Login']").click()
driver.find_element("id", "login_email").send_keys("harry@baltech.in")
driver.find_element("id", "login_password").send_keys("123456")
driver.find_element("id", "login_button").click()

time.sleep(4)

driver.find_element("xpath", "//button[@class='js-cookie-consent-agree cookie-consent__agree']").click()
driver.find_element("xpath", "//a[normalize-space()='Promote Music']").click()

time.sleep(2)

driver.find_element("xpath", "//section[@class='main-container-section clearfix no-padding']//div[2]//div[1]//div[2]//a[1]").click()

time.sleep(2)

driver.find_element("xpath", "//div[@class='table-row spotify_growth_track']//a[@class='button button-primary'][normalize-space()='SELECT']").click()

time.sleep(3)

driver.find_element("id", "next_box_button_facebook-account-connect").click()
driver.find_element("id", "track_url").send_keys("https://open.spotify.com/track/79RUMZfMNMpqZnswovvTqv?si=5c9b4cfd87fc4cc3")
time.sleep(3)

driver.find_element("xpath", "//button[contains(@title,'Select genre')]").click()
driver.find_element("xpath", "//span[normalize-space()='Bass']").click()
driver.find_element("id", "next_box_button_music").click()

time.sleep(2)


driver.close()
driver.quit()
print("Task completed")

