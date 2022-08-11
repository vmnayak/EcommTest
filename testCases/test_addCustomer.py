import random
import string
import time

import pytest
from selenium.webdriver.common.by import By
from faker import Faker
from pageObject.AddCustomerPage import AddCustomer
from pageObject.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        fake = Faker()
        self.logger.info('*Test_003_AddCustomer*')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info('*Logged in Successfully*')

        self.logger.info('*Starting Add Customer Test*')

        self.addcst = AddCustomer(self.driver)

        self.addcst.clickCustomersMenu()
        self.addcst.clickCustomersMenuItem()
        self.addcst.clickAddnew()

        self.logger.info('*Providing Customer Info*')
        self.email = random_generator() + '@gmail.com'
        # self.addcst.setEmail(self.email)
        self.addcst.setEmail(fake.email())
        self.addcst.setPassword('Test123')
        self.addcst.setFirstname(fake.first_name())
        self.addcst.setLastName(fake.last_name())
        self.addcst.setDOB('05/05/2022')
        self.addcst.setGender('Female')
        self.addcst.setCompanyname('RetroShipments')
        self.addcst.setTax(True)
        self.addcst.setIsActive(True)
        self.addcst.setCustomerRole('Administrators')
        self.addcst.setCustomerRole('Vendors')
        self.addcst.setCustomerRole('Forum Moderators')
        self.addcst.setManagerofVendor('Vendor 1')
        self.addcst.setAdminComment('Testing this module...')
        self.addcst.clickSave()

        self.logger.info('*Saving Customer Info*')

        self.msg = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']").text
        print(self.msg)

        if 'customer has been added successfully' in self.msg:
            assert True
            self.logger.info('*Add Customer Test Passed')
        else:
            self.driver.save_screenshot('./Screenshots/'+'test_addCustomer_scr.png')
            self.logger.info('*Add Customer Test Failed')
            assert False

        time.sleep(3)
        self.driver.close()
        self.logger.info('*Ending Add Customer Test*')
