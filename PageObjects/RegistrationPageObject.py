import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Utils.WaitUntil import WaitUntil


class RegistrationPageObject():
    _driver = None

    # Locators
    _registrationPageTitle = (By.CLASS_NAME, 'newsTitle')
    _loginInputField = (By.ID, 'name')
    _loginValidationButton = (By.CLASS_NAME, 'bbcodes')
    _loginValidationMessage = (By.ID, 'result-registration')
    _passwordInputField = (By.NAME, 'password1')
    _emailInputField = (By.NAME, 'email')
    _questionTextLabel = (By.XPATH, "//div[contains(text(),'Наруто')]")
    _answerInputField = (By.NAME, 'question_answer')
    _registerInputButton = (By.NAME, 'submit')
    _ErrorInfoBox = (By.CLASS_NAME, 'ui-dialog')
    _ErrorInfoMessage = (By.ID, 'dle_popup')
    _RegistrationErrorMessage = (By.XPATH, "//*[contains(text(),'Ошибка регистрации')]")

    def __init__(self, driver: webdriver.Remote):
        self._driver = driver


    def GetRegistrationPageTitle(self):
        return WaitUntil.GetElementText(webdriver=self._driver,
                                        locator= self._registrationPageTitle,
                                        timeOutInSeconds=10)

    def Registrate(self, login, password, email, answer):
        WaitUntil.InputText(webdriver=self._driver, locator= self._loginInputField, text= login, timeOutInSeconds= 10)
        WaitUntil.ClickElement(webdriver=self._driver, locator= self._loginValidationButton, timeOutInSeconds= 10)
        WaitUntil.InputText(webdriver=self._driver, locator= self._passwordInputField, text= login, timeOutInSeconds= 10)
        WaitUntil.InputText(webdriver=self._driver, locator= self._emailInputField, text= login, timeOutInSeconds= 10)
        WaitUntil.InputText(webdriver=self._driver, locator= self._answerInputField, text= login, timeOutInSeconds= 10)
        # There's should be some waiting for captcha status OK
        WaitUntil.ClickElement(webdriver=self._driver, locator=self._registerInputButton, timeOutInSeconds=10)

        if (WaitUntil.IsElementVisible(webdriver=self._driver, locator=self._ErrorInfoBox, timeOutInSeconds=5)):
            return WaitUntil.GetElementText(webdriver=self._driver, locator=self._ErrorInfoMessage, timeOutInSeconds= 10);

        return "Registration submitted successfully."

    def IsRegistrationPageTitleDisplayed(self):
        return WaitUntil.IsElementVisible(self._driver, self._registrationPageTitle, 10)

    # Some methods will be added soon
