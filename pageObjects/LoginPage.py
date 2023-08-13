from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    login = (By.LINK_TEXT, "Log in")
    email_address = (By.CSS_SELECTOR, "#Email")
    password = (By.CSS_SELECTOR, "#Password")
    loginBtn = (By.CSS_SELECTOR, ".login-button")

    def loginButton(self):
        return self.driver.find_element(*LoginPage.login)

    def emailField(self):
        return self.driver.find_element(*LoginPage.email_address)

    def passwordField(self):
        return self.driver.find_element(*LoginPage.password)

    def signIn(self):
        return self.driver.find_element(*LoginPage.loginBtn)
