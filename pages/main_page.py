from pages.base_page import BasePage



class MainPage(BasePage):
    class MainPage(BasePage):
        # не осталось никаких м-дов, поэтому оставили заглушку
        # __init__ м-д вызывается при создании объекта
        # ключевое слово super вызывает конструктор класса предка и передает ему все аргументы,
        # кот. передали в конструктор MainPage
        def __init__(self, *args, **kwargs):
            super(MainPage, self).__init__(*args, **kwargs)
