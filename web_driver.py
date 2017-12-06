from selenium import webdriver
from operator_conf import Oper
import pytest

class Init_driver:

    def __init__(self):
        self.browser_name = Oper().getConfig("browser","browser_lis")
        print "self.browser_name:>>>>>>>>",self.browser_name
        
        #config读出的value默认字符串，a="x" eval(a)会报错，config默认写入[x]方式
        if isinstance(eval(self.browser_name),list):
            self.driver = [self.init_driver(i.strip()) for i in eval(self.browser_name)]

    def init_driver(self,name):

        if name == "chrome":
            return webdriver.Chrome(executable_path="/Users/finup/Downloads/chromedriver")
        elif name == "firefox":
            return webdriver.Firefox(executable_path="/Users/finup/Downloads/geckodriver")

    def get_driver(self):
        return self.driver
