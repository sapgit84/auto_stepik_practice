import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # parser.addoption('--browser_name', action='store', default=None,
    # help="Choose browser: '--browser_name=chrome' or '--browser_name=firefox'")

    parser.addoption('--language', action='store', default=None,
                     help="Choose language: '--language=en' or '--language=ru'")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    print("\nstart browser for test..")
    yield browser
    print("\nquit browser..")
    browser.quit()
