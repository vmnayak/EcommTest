from selenium.webdriver.common.by import By


class SearchCustomer:
    txt_email_xpath = "//input[@id='SearchEmail']"
    txt_firstname_xpath = "//input[@id='SearchFirstName']"
    txt_lastname_xpath = "//input[@id='SearchFirstName']"
    btn_search_xpath = "//button[@id='search-customers']"
    table_xpath = "//table[@id='customers-grid']"
    table_rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_cols_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def setFirstname(self, firstname):
        self.driver.find_element(By.XPATH, self.txt_firstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_firstname_xpath).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.txt_lastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_lastname_xpath).send_keys(lastname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()

    def getRowsLen(self):
        return len(self.driver.find_elements(By.XPATH, self.table_rows_xpath))

    def getColsLen(self):
        return len(self.driver.find_elements(By.XPATH, self.table_cols_xpath))

    def searchByEmail(self, email):
        flag = False
        for r in range(1, self.getRowsLen() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchByFirstName(self, fname):
        flag = False
        for r in range(1, self.getRowsLen() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            print(f"fname is {fname}: name found is {name}")
            if fname in name:
                flag = True
                break
        return flag
