"""
        1. Testing login functionality with valid credentials
        2. Testing login functionality with invalid credentials
        3. Testing login functionality with empty fields
        4. Testing login functionality with SQL injection in fields
"""
import os
import pytest
from PageObjects.MainMenuPageObject import MainMenuPageObject
from Utils.TestDataGenerator import TestGenerateData

class TestAuthorization:
    def test_JTA_1_LoginValidData(self, driver_setup):
        # Login
        main_menu = MainMenuPageObject(driver=driver_setup)
        sign_in_page = main_menu.SignIn()

        sign_in_page.Login(login=os.getenv("VALID_LOGIN"), password=os.getenv("VALID_PASSWORD"))

        assert main_menu.IsProfileButtonDisplayed() is True, "Profile button is not appeared"

        # Checking if we are already logged in
        profile_page = main_menu.GoToProfile()

        assert profile_page.IsProfileTitleDisplayed() is True
        assert "/user/JamesGrey" in profile_page.GetPageUrl()

    def test_JTA_2_CheckProfileData(self, driver_setup):
        main_menu = MainMenuPageObject(driver=driver_setup)
        sign_in_page = main_menu.SignIn()

        sign_in_page.Login(login=os.getenv("VALID_LOGIN"), password=os.getenv("VALID_PASSWORD"))

        profile_page = main_menu.GoToProfile()

        assert profile_page.GetProfilePageTitle() == os.getenv("EXPECTED_PROFILE_TITLE"), \
            "Profile title is not as expected"
        assert profile_page.IsLogoutButtonDisplayed() is True, "Logout button is not appeared"

    def test_JTA_3_LoginInvalidData(self,driver_setup):
        main_menu = MainMenuPageObject(driver=driver_setup)
        sign_in_page = main_menu.SignIn()

        sign_in_page.Login(login=TestGenerateData.random_string(8, True),
                           password=TestGenerateData.random_password(8))

        assert main_menu.IsErrorMessageDisplayed() is True, "Error message is not appeared"
        assert os.getenv("EXPECTED_ERROR_MESSAGE") in main_menu.GetErrorMessageText(),\
            "Error message text is not as expected."

    @pytest.mark.parametrize('login, password', [
        ("", ""),
        (" ", " "),
        ("", os.getenv("VALID_PASSWORD")),
        (os.getenv("VALID_LOGIN"),"")
    ])

    def test_JTA_4_LoginEmptyDataFields(self,driver_setup, login, password):
        main_menu = MainMenuPageObject(driver=driver_setup)
        sign_in_page = main_menu.SignIn()

        sign_in_page.Login(login= login,password= password)

        debugInfo = f"Login: '{login}', Password: '{password}'"

        assert main_menu.IsErrorMessageDisplayed() is True, f"Error message is not appeared. {debugInfo}"
        assert os.getenv("EXPECTED_ERROR_MESSAGE") in main_menu.GetErrorMessageText(), \
            f"Error message text is not as expected. {debugInfo}"


    @pytest.mark.parametrize('login, password',[
        (" ' OR '1'='1 ", " ' OR '1'='1 "),
        (" ' OR '1'='1 ", os.getenv("VALID_PASSWORD")),
        (os.getenv("VALID_LOGIN"), " ' OR '1'='1 ")
    ])

    def test_JTA_5_SQLInjectionInFields(self,driver_setup, login, password):
        main_menu = MainMenuPageObject(driver=driver_setup)
        sign_in_page = main_menu.SignIn()

        sign_in_page.Login(login=login, password=password)
        debugInfo = f"Login: '{login}', Password: '{password}'"

        assert main_menu.IsErrorMessageDisplayed() is True, f"Error message is not appeared. {debugInfo}"
        assert os.getenv("EXPECTED_ERROR_MESSAGE") in main_menu.GetErrorMessageText(), \
            f"Error message text is not as expected. {debugInfo}"
