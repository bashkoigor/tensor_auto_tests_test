import pytest

from .pages.main_page import MainPage


class TestCaseSearchInYandex:
    def test_go_to_main_page(self, browser):
        page = MainPage(browser)
        page.open()

    def test_should_be_search_field(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_be_search_field()

    def test_should_be_suggest_block(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_be_search_field()
        page.put_text_and_press_enter('Тензор')
        page.should_be_suggest_block()

    def test_should_be_search_result(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_be_search_field()
        page.put_text_and_press_enter('Тензор')
        page.should_be_search_result()

    @pytest.mark.xfail
    def test_should_be_result_links(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_be_search_field()
        page.put_text_and_press_enter('Тензор')
        page.should_be_search_result()
        page.should_be_link('tensor.ru')



