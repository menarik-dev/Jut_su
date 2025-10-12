import os
from dotenv import load_dotenv
from PageObjects.MainMenuPageObject import MainMenuPageObject
from Utils.TestDataGenerator import TestGenerateData
from UITests.BaseTest import BaseTest
load_dotenv()

EMPTY_DATA_FIELDS = [
    ("", ""),
    (" ", " "),
    ("", os.getenv("VALID_LOGIN")),
    (os.getenv("VALID_PASSWORD"), ""),
]

class AuthorizationTests(BaseTest):

    def test_JTA_1_LoginValidData(self):
        main_menu = MainMenuPageObject(driver=self.driver)
        sign_in = main_menu.SignIn()

        sign_in.Login(login=os.getenv("VALID_LOGIN"), password=os.getenv("VALID_PASSWORD"))

        self.assertTrue(main_menu.IsProfileButtonDisplayed() == True, "Profile button is not appeared")

        profile_page = main_menu.GoToProfile()
        self.assertTrue(profile_page.GetProfilePageTitle() == "JamesGrey")
        self.assertIn("/user/JamesGrey",profile_page.GetPageUrl())

    def test_JTA_2_TestProfileData(self):
        main_menu = MainMenuPageObject(driver=self.driver)
        sign_in = main_menu.SignIn()

        sign_in.Login(login=os.getenv("VALID_LOGIN"), password=os.getenv("VALID_PASSWORD"))

        profile = main_menu.GoToProfile()

        self.assertEqual(profile.GetProfilePageTitle(), "Profile title is not as expected")
        self.assertTrue(profile.IsLogoutButtonDisplayed() == True, "Logout button is not appeared")

        main_menu_after_logout = profile.Logout()

        self.assertTrue(main_menu_after_logout.IsSignInButtonDisplayed() == True, "Sign In button is not appeared after logout")

    def test_JTA_3_LoginInvalidData(self):
        main_menu = MainMenuPageObject(driver=self.driver)
        sign_in = main_menu.SignIn()

        sign_in.Login(login=TestGenerateData.random_string(8, True), password=TestGenerateData.random_password(8))

        self.assertTrue(main_menu.IsErrorMessageDisplayed() == True, "Error message is not appeared")
        self.assertIn(os.getenv("EXPECTED_ERROR_MESSAGE"), main_menu.GetErrorMessageText(), "Error message text is not as expected.")


    def test_JTA_4_LoginEmptyData(self, login, password):
        main_menu = MainMenuPageObject(driver=self.driver)
        sign_in = main_menu.SignIn()

        sign_in.Login(login=login, password=password)