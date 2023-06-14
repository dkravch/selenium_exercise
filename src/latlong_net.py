from .base import BasePage, singleton
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@singleton
class LatLongNetPage(BasePage):

    elements_map = {
        'place_input':      (By.ID, 'place'),
        'place_submit':     (By.ID, 'btnfind'),
        'latitude_output':  (By.ID, 'lat'),
        'longitude_output': (By.ID, 'lng'),
        'lat_long_output':  (By.ID, 'latlngspan'),
        'gps_lat_output':   (By.ID, 'dms-lat'),
        'gps_lng_output':   (By.ID, 'dms-lng'),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattr__(self, item):
        element_type, element_locator = self.elements_map[item]
        return self.driver.find_element(element_type, element_locator)

    def submit_city_name(self, name):
        self.place_input.send_keys(name)
        self.place_submit.click()

    def text_appears_in_lat_long_output(self, text):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element(self.elements_map['lat_long_output'], text)
            )
            return True
        except TimeoutException:
            return False

