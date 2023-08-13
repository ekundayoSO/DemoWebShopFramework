from selenium.webdriver.common.by import By


class DeleteProductsPage:

    def __init__(self, driver):
        self.driver = driver

    checkboxes_xpath = (By.XPATH, "//td/input[@type='checkbox']")
    update_button = (By.CLASS_NAME, "update-cart-button")
    delete_message_element = (By.CLASS_NAME, "order-summary-content")

    def checkboxesElement(self):
        return self.driver.find_elements(*DeleteProductsPage.checkboxes_xpath)

    def updateButtonElement(self):
        return self.driver.find_element(*DeleteProductsPage.update_button)

    def deleteMessage(self):
        return self.driver.find_element(*DeleteProductsPage.delete_message_element)