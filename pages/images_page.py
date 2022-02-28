from .base_page import BasePage
from .locators import ImagesPageLocators


class ImagesPage(BasePage):
    def open_category(self):
        self.browser.find_element(*ImagesPageLocators.FIRST_CATEGORY).click()
        assert "images/search" in self.browser.current_url, f"Category does not open correct, " \
                                                            f"url: {self.browser.current_url}"

    def check_text(self):
        category_text = self.browser.find_element(*ImagesPageLocators.FIRST_CATEGORY_TEXT).text
        search_text = self.browser.find_element(*ImagesPageLocators.IMAGES_SEARCH_FIELD).get_attribute('value')
        assert category_text == search_text, f"Search field contain '{search_text}', expected '{search_text}'"

    def click_firs_image(self):
        self.browser.find_element(*ImagesPageLocators.FIRST_IMAGE).click()
        assert self.is_element_present(*ImagesPageLocators.IMAGE_ORIGIN), "Image does not open correct."

    def image_should_be_change(self):
        self.change_image(ImagesPageLocators.SLIDER_BUTTON_NEXT)
        self.change_image(ImagesPageLocators.SLIDER_BUTTON_PREV)

    def change_image(self, locator):
        src = self.get_image_src(*ImagesPageLocators.IMAGE_ORIGIN)
        self.browser.find_element(*locator).click()
        new_src = self.get_image_src(*ImagesPageLocators.IMAGE_ORIGIN)
        assert src != new_src, "Image does not changed"

    def get_image_src(self, how, what):
        return self.browser.find_element(how, what).get_attribute('src')


