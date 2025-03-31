import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.navigation_page import NavigationPage


class StartPage(NavigationPage):
    _CONSENT_ACCEPT = "button[data-a-target='consent-banner-accept']"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step
    def accept_consents(self):
        self._click_element(self._CONSENT_ACCEPT)
