import selenium
import  re
from selenium import webdriver
from selenium.webdriver.common.by import By

from Utils.WaitUntil import WaitUntil

class ProfilePageObject():
    _driver = None

    # Locators
    _profileTitle = (By.XPATH, "//div[@class='user-title']")
    _logoutButton = (By.XPATH, "//a[@href='/?action=logout']")

    def __init__(self, driver: webdriver.Remote):
        self._driver = driver
        WaitUntil.WaitPageLoaded(webdriver=self._driver, timeInSeconds=20)

    def IsProfileTitleDisplayed(self):
        return WaitUntil.IsElementVisible(webdriver=self._driver, locator=self._profileTitle, timeOutInSeconds=5)

    def IsLogoutButtonDisplayed(self):
        return WaitUntil.IsElementVisible(webdriver=self._driver, locator=self._logoutButton, timeOutInSeconds=5)

    def GetPageUrl(self):
        profileUrl = self._driver.current_url
        return profileUrl

    def GetProfilePageTitle(self):
        profileTitle = WaitUntil.GetElementText(webdriver=self._driver, locator=self._profileTitle, timeOutInSeconds=5)
        return re.sub(r'\s+', ' ', profileTitle).strip()

    def Logout(self):
        from PageObjects.MainMenuPageObject import MainMenuPageObject
        WaitUntil.ClickElement(webdriver=self._driver, locator=self._logoutButton, timeOutInSeconds=5)
        return MainMenuPageObject(self._driver)