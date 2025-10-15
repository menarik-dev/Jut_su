import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from selenium.webdriver.chrome.webdriver import WebDriver

from Utils.CaptchaByPass import CaptchaByPass
from Utils.WaitUntil import WaitUntil

load_dotenv()

@pytest.fixture(scope='class')
def driver_setup():
    options = Options()
    options.add_argument("--incognito")
    # options.add_argument("--headless")
    options.add_argument("--enable-automation")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options)
    CaptchaByPass.PassCaptcha(driver=driver) # Pass captcha by javascript before page loading
    driver.get(os.getenv("BASE_URL"))

    yield driver # передает параметр тестам

    # Same as TearDown
    if driver:
        driver.quit()

@pytest.fixture(scope='function', autouse=True)
def foreachtest(driver_setup):
    driver_setup.delete_all_cookies()
    driver_setup.get(os.getenv("BASE_URL"))
    WaitUntil.WaitPageLoaded(webdriver=driver_setup, timeInSeconds=20)
    yield