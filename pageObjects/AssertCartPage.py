from selenium.webdriver.common.by import By


class AssertCartPage:

    def __init__(self, driver):
        self.driver = driver

    link_shopping_cart = (By.LINK_TEXT, "Shopping cart")
    products_in_cart = (By.CSS_SELECTOR, "td:nth-child(3) a")

    def shoppingCart(self):
        return self.driver.find_element(*AssertCartPage.link_shopping_cart)

    def cartItems(self):
        return self.driver.find_elements(*AssertCartPage.products_in_cart)
