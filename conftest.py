# -*- coding: utf-8 -*-
import pytest
from web_driver import Init_driver
from selenium import webdriver
from operator_conf import Oper

browser = None

def pytest_cmdline_main(config):
    # 从命令行参数中取参数值
    global browser
    browser=config.getoption("--browser")[0]
    print ">>>>>>>>>>>>2222"
def pytest_addoption(parser):
    # 添加参数
    parser.addoption("--browser", action="append",default = [], help="run by browser driver")
    print ">>>>>>>>>>>>11111"
def pytest_generate_tests(metafunc):
    # 将参数添加到parametrize
    if 'browser' in metafunc.fixturenames:
        metafunc.parametrize("browser", metafunc.config.option.browser)
    print ">>>>>>>>>>>>333333"
    update_browser()

# @pytest.fixture(scope='class')
def update_browser():
    if "_" not in browser:
        Oper().insertConfig("browser","browser_lis",[browser.strip()])
    else:
        Oper().insertConfig("browser", "browser_lis", [i.strip() for i in browser.split("_")])
    print ">>>>>>>>>>>>>>>browser update<<<<<<<<<<<<<<"
def pytest_runtest_setup():
    pass