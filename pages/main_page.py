from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver import Keys


class MainPage(BasePage):
    def should_be_search_field(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_FIELD), "Search field does not exist."

    def should_be_suggest_block(self):
        assert self.is_element_present(*MainPageLocators.SUGGEST_BLOCK), "Suggest block does not exist."

    def enter_text(self, text):
        self.browser.find_element(*MainPageLocators.SEARCH_FIELD).send_keys(text)

    def should_be_search_result(self):
        self.browser.find_element(*MainPageLocators.SEARCH_FIELD).send_keys(Keys.ENTER)
        assert 'search' in self.browser.current_url, "Search result does not exist."





