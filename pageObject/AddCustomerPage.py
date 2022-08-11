import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomer:
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']"
    btn_addnew_xpath = "//a[@href='/Admin/Customer/Create']"

    txt_email_xpath = "//input[@id='Email']"
    txt_password_xpath = "//input[@id='Password']"
    txt_firstname_xpath = "//input[@id='FirstName']"
    txt_lastname_xpath = "//input[@id='LastName']"

    rd_male_xpath = "//input[@id='Gender_Male']"
    rd_female_xpath = "//input[@id='Gender_Female']"

    txt_dateofbirth_xpath = "//input[@id='DateOfBirth']"
    txt_companyname_xpath = "//input[@id='Company']"

    chk_istaxexempt_xpath = "//input[@id='IsTaxExempt']"

    txt_newsletter_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
    lst_newsletter_yourname_xpath = "//li[contains(text(),'Your store name')]"
    lst_newsletter_teststore2_xpath = "//li[contains(text(),'Test store 2')]"

    txt_cstRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lst_roles_administrator_xpath = "//li[contains(text(),'Administrators')]"
    lst_roles_registered_xpath = "//li[contains(text(),'Registered')]"
    lst_roles_fmoderator_xpath = "//li[contains(text(),'Forum Moderators')]"
    lst_roles_guest_xpath = "//li[contains(text(),'Guests')]"
    lst_roles_vendors_xpath = "//li[contains(text(),'Vendors')]"

    drp_mgrofVendor_xpath = "//select[@id='VendorId']"
    chk_isActive_xpath = "//input[@id='Active']"

    txtarea_admcomment_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//button[@name='save']"
    role_item = None

    def __init__(self, driver):
        self.driver = driver

    def clickCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickAddnew(self):
        self.driver.find_element(By.XPATH, self.btn_addnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def setPassword(self, pwd):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(pwd)

    def setFirstname(self, firstname):
        self.driver.find_element(By.XPATH, self.txt_firstname_xpath).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.txt_lastname_xpath).send_keys(lastname)

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.txt_dateofbirth_xpath).send_keys(dob)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.rd_male_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rd_female_xpath).click()

    def setCompanyname(self, companyname):
        self.driver.find_element(By.XPATH, self.txt_companyname_xpath).send_keys(companyname)

    def setTax(self, taxexempt):
        if taxexempt:
            self.driver.find_element(By.XPATH, self.chk_istaxexempt_xpath).click()
        else:
            ...

    def setIsActive(self, isActive):
        if isActive:
            ...
        else:
            self.driver.find_element(By.XPATH, self.chk_isActive_xpath).click()

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def setCustomerRole(self, role):
        self.driver.find_element(By.XPATH, self.txt_cstRoles_xpath).click()
        time.sleep(2)

        if role == 'Registered':
            self.role_item = self.driver.find_element(By.XPATH, self.lst_roles_registered_xpath)
        elif role == 'Administrators':
            self.role_item = self.driver.find_element(By.XPATH, self.lst_roles_administrator_xpath)
        elif role == 'Vendors':
            self.role_item = self.driver.find_element(By.XPATH, self.lst_roles_vendors_xpath)
        elif role == 'Forum Moderators':
            self.role_item = self.driver.find_element(By.XPATH, self.lst_roles_fmoderator_xpath)
        elif role == 'Guests':
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//span[contains(.,'Registered')]/following-sibling::span").click()
            self.role_item = self.driver.find_element(By.XPATH, self.lst_roles_guest_xpath)
        time.sleep(1)
        # self.role_item.click()
        self.driver.execute_script("arguments[0].click();", self.role_item)

    def setManagerofVendor(self, manager):
        drp = Select(self.driver.find_element(By.XPATH, self.drp_mgrofVendor_xpath))
        drp.select_by_visible_text(manager)

    def setAdminComment(self, adm_comment):
        self.driver.find_element(By.XPATH, self.txtarea_admcomment_xpath).send_keys(adm_comment)
