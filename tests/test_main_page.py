import pytest
from pages.main_page import MainPage


class TestCaseSearchInYandex:
    def test_should_be_search_field(self, browser):
        """Проверка наличия поля поиска"""
        page = MainPage(browser)
        page.open()
        page.should_be_search_field()

    def test_should_be_suggest_block(self, browser):
        """Проверка наличия блока подсказок"""
        page = MainPage(browser)
        page.open()
        page.enter_text('Тензор')
        page.should_be_suggest_block()

    def test_should_be_search_result(self, browser):
        """Проверка наличия страницы с результатом поиска"""
        page = MainPage(browser)
        page.open()
        page.enter_text('Тензор')
        page.should_be_search_result()

    @pytest.mark.xfail
    def test_should_be_result_links(self, browser):
        """Проверка наличия ссылки в результате поиска"""
        page = MainPage(browser)
        page.open()
        page.enter_text('Тензор')
        page.should_be_link('tensor.ru')



