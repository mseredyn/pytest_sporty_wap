from selenium import webdriver


class WebDriverConfig:

    @classmethod
    def get_chrome_mobile_driver(cls):
        mobile_device = {
            "deviceName": "iPhone X"
        }
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--force-dark-mode')
        chrome_options.add_experimental_option("mobileEmulation", mobile_device)
        chrome_driver = webdriver.Chrome(options=chrome_options)
        return chrome_driver
