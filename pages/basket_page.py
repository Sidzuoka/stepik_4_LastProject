from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_not_be_product_basket()
        self.should_be_text_empty_basket()

    def should_not_be_product_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_BASKET), \
            "Product in the basket, but should not be"

    def should_be_text_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            "Should be text: Your basket is empty."


