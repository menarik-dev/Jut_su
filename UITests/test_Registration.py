# import os
# import time
#
# import pytest
#
# from PageObjects.AuthorizationPageObject import AuthorizationPageObject
# from PageObjects.MainMenuPageObject import MainMenuPageObject
# from Utils.TestDataGenerator import TestGenerateData
#
# class TestRegistration:
#     def test_JTR_1_RegistrateValidData(self, driver_setup):
#         main_menu = MainMenuPageObject(driver_setup)
#         main_menu.SignIn()
#
#         registration_page = AuthorizationPageObject(driver_setup).GoToRegistrationPage()
#
#         registration_page.Registrate("TestUser123", "TestPassword1234", "test@exaple.com", "Наруто")
#
#         assert "Регистрация" in registration_page.GetRegistrationPageTitle()