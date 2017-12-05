import pytest
from selenium import webdriver
import time,threading
from Utils.logg import log_message
from web_driver import Init_driver
from start_thread import thread_start

class Test_ABC():

    def setup_class(self):
        self.dr = Init_driver().get_driver()
    def teardown_class(self):
        if isinstance(self.dr,list):
            for i in self.dr:
                i.close()
        else:
            self.dr.close()

    def searchx(self, chrome_driver, url, data):
        chrome_driver.get(url)
        print chrome_driver.name
        print chrome_driver.title
        chrome_driver.find_element_by_id("kw").send_keys(data)
        time.sleep(5)
        assert 1
    def searchy(self, chrome_driver, url, data):
        chrome_driver.get(url)
        print chrome_driver.name
        print chrome_driver.title
        chrome_driver.find_element_by_id("search-input").send_keys(data)
        time.sleep(5)
        assert 1

    @pytest.mark.parametrize('url,data', [("http://www.baidu.com", "hahahah"), ("http://www.baidu.com", "asdasda")])
    def test_a(self, url, data):
        thread_start(self.dr, self.searchx, url, data)

    @pytest.mark.parametrize('url,data', [("https://www.hao123.com", "hahahah"), ("https://www.hao123.com", "asdasda")])
    def test_b(self, url, data):
        thread_start(self.dr, self.searchy, url, data)


