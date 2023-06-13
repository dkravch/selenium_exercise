import time


def test_dummy_local(lat_long_page):
    lat_long_page.open()
    lat_long_page.submit_city_name('Kyiv')
    assert lat_long_page.text_appears_in_lat_long_output("(50.447731, 30.542721)")


def test_dummy_remote(remote_driver):
    remote_driver.get('http://www.google.com/')
    time.sleep(5)  # Let the user actually see something!
    search_box = remote_driver.find_element("name", "q")
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5)  # Let the user actually see something!
    assert True

