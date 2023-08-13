from selenium.webdriver.common.by import By


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    link_register_class = (By.CLASS_NAME, "ico-register")
    radioButton_gender_id = (By.ID, "gender-male")
    textbox_firstName_id = (By.ID, "FirstName")
    textbox_lastName_id = (By.ID, "LastName")
    textbox_email_id = (By.ID, "Email")
    textbox_password_id = (By.ID, "Password")
    textbox_confirmPassword_id = (By.ID, "ConfirmPassword")
    button_register_id = (By.ID, "register-button")
    element_registration_message_class = (By.CLASS_NAME, "result")
    link_logout_class = (By.CLASS_NAME, "ico-logout")

    def clickRegisterLinkText(self):
        return self.driver.find_element(*RegistrationPage.link_register_class)

    def selectGender(self):
        return self.driver.find_element(*RegistrationPage.radioButton_gender_id)

    def enterFirstName(self):
        return self.driver.find_element(*RegistrationPage.textbox_firstName_id)

    def enterLastName(self):
        return self.driver.find_element(*RegistrationPage.textbox_lastName_id)

    def enterUserEmail(self):
        return self.driver.find_element(*RegistrationPage.textbox_email_id)

    def enterUserPassword(self):
        return self.driver.find_element(*RegistrationPage.textbox_password_id)

    def enterUserConfirmPassword(self):
        return self.driver.find_element(*RegistrationPage.textbox_confirmPassword_id)

    def clickRegisterButton(self):
        return self.driver.find_element(*RegistrationPage.button_register_id)

    def getRegistrationMessage(self):
        return self.driver.find_element(*RegistrationPage.element_registration_message_class)

    def logOut(self):
        return self.driver.find_element(*RegistrationPage.link_logout_class)
