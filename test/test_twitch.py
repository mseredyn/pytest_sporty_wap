import logging

from pages.search_page import SearchPage
from pages.start_page import StartPage
from pages.streamer_page import StreamerPage

LOGGER = logging.getLogger(__name__)


class TestTwitch:
    def test_twitch_startcraft_stream(self, chrome_mobile_driver):
        start_page = StartPage(chrome_mobile_driver)
        start_page.wait_for_page_to_load()
        start_page.accept_consents()
        start_page.go_to_search_page()

        search_page = SearchPage(chrome_mobile_driver)
        search_page.wait_for_page_to_load()
        search_page.fill_search_input_with("Starcraft II")
        search_page.click_starcraft_2_search_result()
        search_page.wait_for_page_to_load()
        search_page.assert_result_loaded()
        search_page.scroll_by_screen_height()
        search_page.scroll_by_screen_height()
        search_page.click_7th_result()

        streamer_page = StreamerPage(chrome_mobile_driver)
        streamer_page.wait_for_streamer_page_to_load()
        # did not encounter popup to handle
        streamer_page.take_screenshot_of_current_view()
