import time

import pytest
from faker import Faker
from pageObject.AddCustomerPage import AddCustomer
from pageObject.LoginPage import LoginPage
from pageObject.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_005_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_addCustomer(self, setup):
        fake = Faker()
        self.logger.info('*Test_005_SearchCustomerByEmail*')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info('*Logged in Successfully*')

        self.logger.info('*Starting Search By Email Test*')
        self.addcst = AddCustomer(self.driver)
        self.addcst.clickCustomersMenu()
        self.addcst.clickCustomersMenuItem()

        self.logger.info('*Searching By Email*')
        searchcst = SearchCustomer(self.driver)
        searchcst.setEmail('victoria_victoria@nopCommerce.com')
        searchcst.clickSearch()
        time.sleep(3)
        status = searchcst.searchByEmail('victoria_victoria@nopCommerce.com')
        self.driver.close()
        self.logger.info('*TC_SearchCustomerByEmail_005 Finished*')
        assert status



