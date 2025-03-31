import os

import pytest

from config.WebDriverConfig import WebDriverConfig


@pytest.fixture(scope="session")
def chrome_mobile_driver():
    driver = WebDriverConfig.get_chrome_mobile_driver()
    driver.get(os.environ.get("BASE_UI_URL"))
    yield driver
    driver.close()
