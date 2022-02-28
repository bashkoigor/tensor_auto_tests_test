from pages.images_page import ImagesPage
from pages.locators import ImagesPageLocators
from pages.main_page import MainPage


class TestCaseImagesInYandex:
    def test_should_be_images_link(self, browser):
        """Проверка наличия ссылки «Картинки»"""
        page = MainPage(browser)
        page.open()
        page.should_be_images_link()

    def test_is_images_page(self, browser):
        """Проверка перехода на страницу «Картинки»"""
        page = MainPage(browser)
        page.open()
        page.go_to_images_page()
        page.is_current_link(ImagesPageLocators.IMAGES_LINK)

    def test_open_first_category_check_text(self, browser):
        """Проверка открытия категорий и соответствия текста в поиске"""
        page = MainPage(browser)
        page.open()
        page.go_to_images_page()
        images_page = ImagesPage(browser)
        images_page.open_category()
        images_page.check_text()

    def test_open_image(self, browser):
        """Проверка открытия изображения"""
        page = ImagesPage(browser, ImagesPageLocators.IMAGES_LINK)
        page.open()
        page.open_category()
        page.click_firs_image()
        page.image_should_be_change()




