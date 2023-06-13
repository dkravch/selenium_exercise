import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from .src.latlong_net import LatLongNetPage

import os
import sys

ABS_PATH = os.path.dirname(os.path.abspath(__file__))
driver_fullpath = os.path.join(ABS_PATH, 'bin/chromedriver')
print(driver_fullpath)
sys.path.append(driver_fullpath)

########################################################################################################################


@pytest.fixture(scope="session", autouse=False)
def base_url():
    return 'https://google.com'


@pytest.fixture(scope="session", autouse=False)
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="session", autouse=False)
def remote_driver():
    remote_driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
    yield remote_driver
    remote_driver.quit()


@pytest.fixture(scope="session", autouse=False)
def lat_long_page(driver):
    yield LatLongNetPage(driver, 'https://www.latlong.net/')
