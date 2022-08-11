import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    global driver

    if browser == 'chrome':
        serv_obj = Service('C:/SeleniumPython/Drivers/chromedriver_win32/chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        print("Launching Chrome")

    elif browser == 'firefox':
        serv_obj = Service('C:/SeleniumPython/Drivers/geckodriver-v0.31.0-win64/geckodriver.exe')
        driver = webdriver.Firefox(service=serv_obj)
        print("Launching Firefox")

    else:
        serv_obj = Service('C:/SeleniumPython/Drivers/edgedriver_win64/msedgedriver.exe')
        driver = webdriver.Edge(service=serv_obj)
        print("Launching Edge")

    return driver


def pytest_addoption(parser):  # to get value from CLI/

    parser.addoption('--browser')


@pytest.fixture()
def browser(request):  # this will return Browser value to the setup method
    return request.config.getoption('--browser')


# Pytest HTML reports
# add hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module'] = 'Customers'
    config._metadata['Tester'] = 'Vijay'


# optional hook to delete/edit environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
