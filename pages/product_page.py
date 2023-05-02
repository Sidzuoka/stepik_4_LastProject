from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from pages.locators import MainPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.add_to_basket()

    def should_be_product_url(self):
        assert "?promo=offer" in self.browser.current_url, "Not correct url"

    def add_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button_basket.click()

    def should_be_product_name(self):
        product_name = self.browser.find_element(*MainPageLocators.PRODUCT_NAME)
        product_name_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        print(product_name_basket.text)
        assert product_name.text == product_name_basket.text, f"Should be product name: '{product_name.text}'"

    def should_be_product_price(self):
        product_price = self.browser.find_element(*MainPageLocators.PRODUCT_PRICE)
        product_price_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert product_price.text == product_price_basket.text, f"Should be product price: 19.99"

