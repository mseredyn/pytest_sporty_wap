import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base_page import BasePage


class NavigationPage(BasePage):
    _SEARCH_BUTTON = "//a[.//div[text()='Przeglądaj']]"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step
    def go_to_search_page(self):
        self._click_element(self._SEARCH_BUTTON)
