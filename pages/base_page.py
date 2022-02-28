from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from .locators import MainPageLocators, BasePageLocators


class BasePage:
    def __init__(self, browser, url=BasePageLocators.URL, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_images_page(self):
        self.browser.find_element(*MainPageLocators.IMAGES_LINK).click()
        self.browser.switch_to.window(self.browser.window_handles[1])

    def is_current_link(self, link):
        assert link in self.browser.current_url, f"Link {link} is not current"

    def should_be_link(self, link):
        pool = []
        for i in range(3, 8):
            element = self.browser.find_element(By.CSS_SELECTOR, f"#search-result > li:nth-child({i}) a")
            pool.append(link in element.get_attribute("href"))
        assert all(pool), f'The first five links do not link to {link}'

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
