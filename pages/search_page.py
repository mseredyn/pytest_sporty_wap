import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.navigation_page import NavigationPage


class SearchPage(NavigationPage):
    _SEARCH_INPUT = "input[type='search']"
    _STARCRAFT_2_LIST_RESULT = "a[href='/directory/category/starcraft-ii']"
    _STARCRAFT_2_RESULT_HEADER = "//main//h1"
    _STARCRAFT_2_7TH_RESULT = "((//article)[7]//a[contains(@href, 'home')])[1]"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step
    def fill_search_input_with(self, value_to_fill: str):
        self._fill_element(self._SEARCH_INPUT, value_to_fill)

    @allure.step
    def click_starcraft_2_search_result(self):
        self._click_element(self._STARCRAFT_2_LIST_RESULT)

    @allure.step
    def assert_result_loaded(self):
        self._assert_text(self._STARCRAFT_2_RESULT_HEADER, "StarCraft II")

    @allure.step
    def click_7th_result(self):
        self._click_element(self._STARCRAFT_2_7TH_RESULT)
