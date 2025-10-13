import selenium
import  re
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utils.WaitUntil import WaitUntil

class AuthorizationPageObject():
    # Locators
    _loginInputField = (By.XPATH,"//input[@name='login_name']")
    _passwordInputField = (By.XPATH,"//input[@name='login_password']")
    _loginInputButton = (By.XPATH,"//input[@id='login_submit']")
    _registrationLinkButton = (By.XPATH,"//a[@href='/register.html']")

    def __init__(self, driver: webdriver.Remote):
        self._driver = driver

    def Login(self, login, password):
        from PageObjects.MainMenuPageObject import MainMenuPageObject

        WaitUntil.InputText(webdriver=self._driver, locator=self._loginInputField, text=login, timeOutInSeconds=10)
        WaitUntil.InputText(webdriver=self._driver, locator=self._passwordInputField, text=password, timeOutInSeconds=10)
        WaitUntil.ClickElement(webdriver=self._driver, locator=self._loginInputButton, timeOutInSeconds=10)
        return MainMenuPageObject(self._driver)

    def GoToRegistrationPage(self):
        from PageObjects.RegistrationPageObject import RegistrationPageObject

        WaitUntil.ClickElement(webdriver=self._driver, locator=self._registrationLinkButton, timeOutInSeconds=10)
        return RegistrationPageObject(self._driver)
