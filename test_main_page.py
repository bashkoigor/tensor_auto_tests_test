from .pages.main_page import MainPage


def test_go_to_main_page(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
