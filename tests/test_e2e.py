import time

from selenium.webdriver import Keys

from pageObjects.AddProductsPage import AddToCartPage
from pageObjects.AssertCartPage import AssertCartPage
from pageObjects.DeleteProductsPage import DeleteProductsPage
from pageObjects.LoginPage import LoginPage
from pageObjects.assertProductsPricesPage import AssertProductsPricesPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_login(self):

        # Login
        login_obj = LoginPage(self.driver)
        login_obj.loginButton().click()
        login_obj.emailField().send_keys("sfvf@gmail.com")
        login_obj.passwordField().send_keys("Abc@123")
        login_obj.signIn().click()

    def test_e2e(self):

        log = self.getLogger()
        # Add products to shopping cart
        products = ["Health Book",
                    "Smartphone",
                    "Blue Jeans",
                    "Casual Golf Belt",
                    "Genuine Leather Handbag",
                    "Black & White Diamond Heart"]
        log.info("Getting all products names")

        for product in products:
            cart_object = AddToCartPage(self.driver)
            time.sleep(5)
            search_box = cart_object.searchField()
            search_box.send_keys(product)
            search_box.send_keys(Keys.RETURN)
            time.sleep(5)
            add_to_cart_button = cart_object.addToCartButton()
            add_to_cart_button.click()

        # Assert products in shopping cart
        expected_products_list = ["Health Book",
                                  "Smartphone",
                                  "Blue Jeans",
                                  "Casual Golf Belt",
                                  "Genuine Leather Handbag with Cell Phone Holder & Many Pockets",
                                  "Black & White Diamond Heart"]
        actual_products_List = []

        assertion_obj = AssertCartPage(self.driver)
        assertion_obj.shoppingCart().click()

        cart_products = assertion_obj.cartItems()

        for cart_product in cart_products:
            product_names = cart_product.text
            log.info(product_names)
            actual_products_List.append(product_names)

        assert expected_products_list == actual_products_List, "Expected products do not match actual in cart."

        # Assert products prices in shopping cart
        prices_obj = AssertProductsPricesPage(self.driver)
        assertion_obj.shoppingCart().click()
        prices = prices_obj.pricesList()
        subTotal = float(prices_obj.actualTotalPrice().text)

        summation = 0
        for price in prices:
            summation = summation + float(price.text)
            log.info(summation)

        assert summation == subTotal

        # Delete products from shopping cart
        assertion_obj.shoppingCart().click()
        box_obj = DeleteProductsPage(self.driver)
        checkboxes = box_obj.checkboxesElement()

        for checkbox in checkboxes:
            checkbox.click()

        box_obj.updateButtonElement().click()

        message = box_obj.deleteMessage().text
        assert "Your Shopping Cart is empty!" in message
        log.info(message)
