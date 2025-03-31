import datetime
import time

import allure
from hamcrest import assert_that, equal_to
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step
    def _get_element(self, selector: str):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=0.1)
        wait.until(expected_conditions.presence_of_element_located((self._by_chooser(selector), selector)))
        wait.until(expected_conditions.visibility_of_element_located((self._by_chooser(selector), selector)))
        return self.driver.find_element(self._by_chooser(selector), selector)

    @allure.step
    def _get_elements(self, selector: str):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=0.1)
        wait.until(expected_conditions.presence_of_all_elements_located((self._by_chooser(selector), selector)))
        wait.until(expected_conditions.visibility_of_all_elements_located((self._by_chooser(selector), selector)))
        return self.driver.find_elements(self._by_chooser(selector), selector)

    @allure.step
    def _click_element(self, selector):
        self._get_element(selector).click()

    @allure.step
    def _fill_element(self, selector, value_to_fill):
        self._get_element(selector).clear()
        self._get_element(selector).send_keys(value_to_fill)

    @allure.step
    def _assert_text(self, selector, expected_text):
        actual_text = self._get_element(selector).text
        assert_that(actual_text, equal_to(expected_text))

    @allure.step
    def scroll_by_screen_height(self):
        current_scroll = int(self.driver.execute_script("return document.documentElement.scrollHeight"))
        self.driver.execute_script(f'window.scrollTo(0, {self.driver.get_window_size()["height"] + current_scroll})')

    @allure.step
    def take_screenshot_of_current_view(self):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
        self.driver.save_screenshot(f'{timestamp}screenshot.png')

    @allure.step
    def wait_for_page_to_load(self):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=0.1)
        wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

    @classmethod
    def _by_chooser(cls, selector: str):
        if selector.startswith("/") or selector.startswith("("):
            return By.XPATH
        else:
            return By.CSS_SELECTOR
