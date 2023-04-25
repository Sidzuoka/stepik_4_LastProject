from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def go_to_login_page(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        # передали именно пару, и этот кортеж нужно распаковать
        login_link.click()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Not correct url"
        # реализуйте проверку на корректный url адрес (в url должен быть login)
        # .browser.current_url - забирает строку url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        # реализуйте проверку, что есть форма логина

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
        # реализуйте проверку, что есть форма регистрации на странице
