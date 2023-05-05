from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_not_be_product_basket()
        self.should_be_text_empty_basket()

    def should_not_be_product_basket(self):
        assert self.is_not_element_present(By.XPATH, "//div[@class='row']/h2"), "Product in the basket, but should not be"

    def should_be_text_empty_basket(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#content_inner p"), "Should be text: Your basket is empty."


