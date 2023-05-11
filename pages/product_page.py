from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import MainPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.add_to_basket()

    def should_be_product_url(self):
        assert "catalogue" in self.browser.current_url, "Should be product page"

    def add_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button_basket.click()

    def should_be_product_name(self):
        product_name = self.browser.find_element(*MainPageLocators.PRODUCT_NAME)
        product_name_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert product_name.text == product_name_basket.text, f"Should be product name: '{product_name.text}'"

    def should_be_product_price(self):
        product_price = self.browser.find_element(*MainPageLocators.PRODUCT_PRICE)
        product_price_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert product_price.text == product_price_basket.text, f"Should be product price: 9.99"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
                "Success message is presented, but should not be"

    def should_not_be_success_message_after_time(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
