# pytest_sporty_wap
This test framework goes into https://www.twitch.tv/ searches for StarCraft II, scrolls two times, enters one of streams
## How to run
* clone repository
* cd into cloned repository
* .\venv\Scripts\activate
* pip3 install -r requirements.txt
* pytest

## Structure
```
pytest_sporty_wap
|-- .env                            # in this case url storage
|-- .gitignore
|-- pytest.ini
|-- README.md
|-- requirements.txt
|
|-- config
|-- |-- WebDriverConfig             # configuration of WebDriver
|
|-- pages
|-- |-- base_page.py                # only class that is allowed to interact with Selenium
|-- |-- navigation_page.py          # subview class that aggregates navigation
|-- |-- search_page.py
|-- |-- start_page.py
|-- |-- stream_page.py
|
|-- test                            # test folder
|-- |-- conftest.py                 # storage for global fixtures, test configurations
|-- |-- test_twich.py               # test itself
```