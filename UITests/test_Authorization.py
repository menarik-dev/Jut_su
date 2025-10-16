import os
import pytest
import allure
from allure_commons.types import Severity

from PageObjects.MainMenuPageObject import MainMenuPageObject
from Utils.TestDataGenerator import TestGenerateData

@allure.epic("User Management")
@allure.feature("Authorization functionality")
class TestAuthorization:
    @allure.story("Login with valid data and check profile link")
    @allure.severity("Critical")
    @allure.tag("smoke", "positive")
    @pytest.mark.positive
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

    @allure.story("Verify profile data after successful login")
    @allure.severity("Normal")
    @pytest.mark.positive
    def test_JTA_2_CheckProfileData(self, driver_setup):
        main_menu = MainMenuPageObject(driver=driver_setup)
        sign_in_page = main_menu.SignIn()

        sign_in_page.Login(login=os.getenv("VALID_LOGIN"), password=os.getenv("VALID_PASSWORD"))

        profile_page = main_menu.GoToProfile()

        assert profile_page.GetProfilePageTitle() == os.getenv("EXPECTED_PROFILE_TITLE"), \
            "Profile title is not as expected"
        assert profile_page.IsLogoutButtonDisplayed() is True, "Logout button is not appeared"

    @allure.story("Login with random invalid credentials")
    @allure.severity("Blocker")
    @pytest.mark.negative
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

    @allure.story("Login with empty or missing data fields")
    @allure.severity("Major")
    @pytest.mark.negative
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

    @allure.story("Prevent SQL injection in login fields")
    @allure.severity("Critical")  # Безопасность критична
    @allure.tag("security", "negative")
    @pytest.mark.negative
    def test_JTA_5_SQLInjectionInFields(self,driver_setup, login, password):
        main_menu = MainMenuPageObject(driver=driver_setup)
        sign_in_page = main_menu.SignIn()

        sign_in_page.Login(login=login, password=password)
        debugInfo = f"Login: '{login}', Password: '{password}'"

        assert main_menu.IsErrorMessageDisplayed() is True, f"Error message is not appeared. {debugInfo}"
        assert os.getenv("EXPECTED_ERROR_MESSAGE") in main_menu.GetErrorMessageText(), \
            f"Error message text is not as expected. {debugInfo}"
