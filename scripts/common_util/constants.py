#  This file conatins constants and import common utilised lib across project  


#  constants
api_request_url = "https://api.github.com/"
webdriver_path = 'input/chromedriver.exe'

# external libs
import requests
import os
import sys
import time
import unittest
from os import path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from scripts.common_util.api_operation import *
from scripts.common_util.ui_helper.browser_helper import *
from scripts.common_util.ui_helper.ui_helper import *

class NumbersTestResult(unittest.TextTestResult):
    def addSubTest(self, test, subtest, outcome):
        # handle failures calling base class
        super(NumbersTestResult, self).addSubTest(test, subtest, outcome)
        # add to total number of tests run
        self.testsRun += 1
