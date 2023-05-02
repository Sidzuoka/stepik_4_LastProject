from .pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('arg', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, arg):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{arg}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.solve_quiz_and_get_code()
    page.should_be_product_name()
    page.should_be_product_price()
