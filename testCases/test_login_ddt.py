import time

import pytest

from pageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = './TestData/LoginData.xlsx'
    # username = ReadConfig.getUserName()
    # password = ReadConfig.getPassword()

    logger = LogGen.loggen()
    logger.info('*Test_002*')

    # @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info('*Test_002_DDT_Login*')
        self.logger.info('*Verifying Login DDT Title*')
        self.logger.info('')
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print(f'No of rows in excel: {self.rows}')
        testcase_status = []
        for row in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', row, 1)
            self.pwd = XLUtils.readData(self.path, 'Sheet1', row, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', row, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.pwd)
            self.lp.clickLogin()
            time.sleep(3)

            act_title = self.driver.title
            if act_title == 'Dashboard / nopCommerce administration':
                self.logger.info('*Logged in Successfully')
                if self.exp == 'pass':
                    self.logger.info('*Login Title Passed*')
                    self.lp.clickLogout()
                    testcase_status.append('Pass')
                else:
                    # self.driver.save_screenshot("./Screenshots/" + "test_loginTitle.png")
                    self.logger.error('*Login Title Failed*')
                    self.lp.clickLogout()
                    testcase_status.append('Fail')
            else:
                if self.exp == 'Pass':
                    self.logger.info('*Test Failed*')
                    testcase_status.append('Fail')
                else:
                    self.logger.info('*Test Passed*')
                    testcase_status.append('Pass')

        if 'Fail' not in testcase_status:
            self.logger.info('*DDT Test Passed')
            self.driver.close()
            assert True
        else:
            self.logger.info('*DDT Test Failed')
            self.driver.close()
            assert False


        # self.driver.close()

    logger.info('*DDT Test Completed')
