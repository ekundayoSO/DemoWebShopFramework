from selenium.webdriver.common.by import By


class AssertProductsPricesPage:

    def __init__(self, driver):
        self.driver = driver

    prices_list_css = (By.CSS_SELECTOR, "td:nth-child(6)")
    prices_subtotal_class = (By.CLASS_NAME, "product-price")

    def pricesList(self):
        return self.driver.find_elements(*AssertProductsPricesPage.prices_list_css)

    def actualTotalPrice(self):
        return self.driver.find_element(*AssertProductsPricesPage.prices_subtotal_class)

