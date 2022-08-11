import pytest

from pageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()
    logger.info('*Test_001*')

    # @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info('*Verifying Homepage Title*')

        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title

        if actual_title == 'Your store. Login':
            self.driver.close()
            self.logger.info('*Homepage Title Test Passed*')

            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.warning('*Homepage Title Test Failed*')
            assert False

        # self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginTitle(self, setup):
        self.logger.info('*Verifying Login Title*')
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title
        if act_title == 'Dashboard / nopCommerce administration':
            self.driver.close()
            self.logger.info('*Login Title Passed*')
            assert True
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_loginTitle.png")
            self.driver.close()
            self.logger.error('*Login Title Failed*')
            assert False

        # self.driver.close()
