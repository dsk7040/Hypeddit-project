class loginpage():

    def __init__(self, driver):
        self.driver = driver

        self.password_dev_textbox_xpath = "//input[@placeholder='Password']"
        self.submit_button_xpath = "//button[normalize-space()='SUBMIT']"
        self.login_dev_button_xpath = "//a[normalize-space()='Login']"
        self.username_textbox_id = "login_email"
        self.password_textbox_id = "login_password"
        self.login_button_id = "login_button"

    def enter_password_dev(self, password):
        #self.driver.find_element(self.password_textbox_xpath).clear()
        self.driver.find_element("xpath",self.password_dev_textbox_xpath).send_keys(password)

    def click_submit(self):
        self.driver.find_element("xpath",self.submit_button_xpath).click()

    def click_login_dev(self):
        self.driver.find_element("xpath",self.login_dev_button_xpath).click()

    def enter_username(self, username):
        self.driver.find_element("id",self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element("id",self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element("id",self.login_button_id).click()
