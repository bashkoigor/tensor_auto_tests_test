from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser, timeout=3):
        self.browser = browser
        self.url = "https://yandex.ru/"
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def should_be_href(self, link):
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
