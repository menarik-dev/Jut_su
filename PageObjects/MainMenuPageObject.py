import selenium
import  re
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.ProfilePageObject import ProfilePageObject

from Utils.WaitUntil import WaitUntil


class MainMenuPageObject():
    # Locators
    _signInButton = (By.XPATH, "//span[contains(text(), 'Войти')]")
    _profileLinkButton = (By.XPATH, "//*[@id='topLoginPanelAvatar']/following::a[contains(text(), 'Профиль')]")
    _ErrorMessage = (By.XPATH, "//div[@class='clear berrors']")

    def __init__(self, driver: webdriver.Remote):
        self._driver = driver

    # Methods checks elements states
    def IsSignInButtonDisplayed(self):
        return WaitUntil.IsElementVisible(webdriver=self._driver, locator= self._signInButton, timeOutInSeconds=5)

    def IsErrorMessageDisplayed(self):
        return WaitUntil.IsElementVisible(webdriver=self._driver, locator= self._ErrorMessage, timeOutInSeconds=5)

    def IsProfileButtonDisplayed(self):
        return WaitUntil.IsElementVisible(webdriver=self._driver, locator= self._profileLinkButton, timeOutInSeconds=5)

    # Methods to get text and other properties of elements

    def GetErrorMessageText(self):
        errorMeessage = WaitUntil.GetElementText(webdriver=self._driver, locator=self._ErrorMessage, timeOutInSeconds=5)
        return re.sub(r'\s+', ' ',  errorMeessage).strip()

    def GetProfileButtonText(self):
        return  WaitUntil.GetElementText(webdriver=self._driver, locator= self._profileLinkButton, timeOutInSeconds=5)

    def GetPageUrl(self):
        url = self._driver.current_url
        return url

    def GetPageTitle(self):
        title = self._driver.title
        return title

    # Navigation methods

    def SignIn(self):
        from PageObjects.AuthorizationPageObject import AuthorizationPageObject
        WaitUntil.ClickElement(webdriver=self._driver, locator=self._signInButton, timeOutInSeconds=5)
        return AuthorizationPageObject(self._driver)

    def GoToProfile(self):
        WaitUntil.ClickElement(webdriver=self._driver, locator=self._profileLinkButton, timeOutInSeconds= 5)
        return ProfilePageObject(self._driver)