from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_FIELD = (By.ID, "text")
    SUGGEST_BLOCK = (By.CLASS_NAME, "mini-suggest__popup_visible")
