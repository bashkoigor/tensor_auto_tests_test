from selenium.webdriver.common.by import By


class BasePageLocators:
    URL = "https://yandex.ru/"


class MainPageLocators:
    SEARCH_FIELD = (By.ID, "text")
    SUGGEST_BLOCK = (By.CLASS_NAME, "mini-suggest__popup_visible")
    IMAGES_LINK = (By.CSS_SELECTOR, 'a[data-id="images"]')


class ImagesPageLocators:
    IMAGES_LINK = "https://yandex.ru/images/"
    FIRST_CATEGORY = (By.CSS_SELECTOR, ".PopularRequestList .PopularRequestList-Item_pos_0")
    FIRST_CATEGORY_TEXT = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0 .PopularRequestList-SearchText")
    IMAGES_SEARCH_FIELD = (By.CLASS_NAME, "input__control")
    FIRST_IMAGE = (By.CLASS_NAME, "serp-item_pos_0")
    IMAGE_ORIGIN = (By.CLASS_NAME, "MMImage-Origin")
    SLIDER_BUTTON_NEXT = (By.CLASS_NAME, "CircleButton_type_next")
    SLIDER_BUTTON_PREV = (By.CLASS_NAME, "CircleButton_type_prev")



