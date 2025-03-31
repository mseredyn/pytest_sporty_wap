from selenium.webdriver.chrome.webdriver import WebDriver

from pages.navigation_page import NavigationPage


class StreamerPage(NavigationPage):
    _OBSERVE_CHANNEL_BUTTON = "button[aria-label='Obserwuj kanał ']"
    _STREAMS = "article"
    _PROFILE_BANNER = "img[alt^='Baner profilu']"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def wait_for_streamer_page_to_load(self):
        self.wait_for_page_to_load()
        self._get_element(self._OBSERVE_CHANNEL_BUTTON)
        self._get_elements(self._STREAMS)
        self._get_element(self._PROFILE_BANNER)
