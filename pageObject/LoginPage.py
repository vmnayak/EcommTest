from selenium.webdriver.common.by import By


class LoginPage:
    txtbox_login_id = "Email"
    txtbox_pass_txt_id = "Password"
    login_btn_Xpath = "//*[@class='button-1 login-button']"
    logout_Linktxt = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.txtbox_login_id).clear()
        self.driver.find_element(By.ID, self.txtbox_login_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txtbox_pass_txt_id).clear()
        self.driver.find_element(By.ID, self.txtbox_pass_txt_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_btn_Xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_Linktxt).click()
