
from selenium.webdriver.common.by import By


class AddToCartPage:

    def __init__(self, driver):
        self.driver = driver

    search_element = (By.CSS_SELECTOR, "#small-searchterms")
    add_to_cart = (By.CSS_SELECTOR, "input[value='Add to cart']")

    def searchField(self):
        return self.driver.find_element(*AddToCartPage.search_element)

    def addToCartButton(self):
        return self.driver.find_element(*AddToCartPage.add_to_cart)

