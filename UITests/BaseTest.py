import os
import  selenium
import unittest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from Utils.WaitUntil import WaitUntil


class BaseTest(unittest.TestCase):
    driver = None
    options = None
    load_dotenv()

    @classmethod
    def setUpClass(cls):
        cls.options = Options()
        cls.options.add_argument("--incognito")
        cls.options.add_argument("--headless")
        cls.options.add_argument("--enable-automation")
        cls.options.add_argument("--no-sandbox")
        cls.options.add_argument("--disable-blink-features=AutomationControlled")
        cls.options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

        cls.driver = webdriver.Chrome(options=cls.options)
        cls.driver.get(os.getenv("BASE_URL"))

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()


    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.get(os.getenv("BASE_URL"))
        WaitUntil.WaitPageLoaded(webdriver=self.driver, timeInSeconds=20)
