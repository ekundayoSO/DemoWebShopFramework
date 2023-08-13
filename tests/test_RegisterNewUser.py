import pytest

from pageObjects.RegistrationPage import RegistrationPage
from testData.RegistrationData import RegistrationData
from utilities.BaseClass import BaseClass


class TestRegisterNewUser(BaseClass):

    def test_formSubmission(self, getData):
        register_object = RegistrationPage(self.driver)
        register_object.clickRegisterLinkText().click()
        register_object.selectGender().click()
        register_object.enterFirstName().send_keys(getData["firstname"])
        register_object.enterLastName().send_keys(getData["lastname"])
        register_object.enterUserEmail().send_keys(getData["email"])
        register_object.enterUserPassword().send_keys(getData["Password"])
        register_object.enterUserConfirmPassword().send_keys(getData["ConfirmPassword"])
        register_object.clickRegisterButton().click()

        message = register_object.getRegistrationMessage().text
        assert "Your registration" in message

        register_object.logOut().click()

    @pytest.fixture(params=RegistrationData.test_Registration_data)
    def getData(self, request):
        return request.param
