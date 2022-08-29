import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default="chrome",
        help="Choose browser: chrome or firefox or IE"
    )
    parser.addoption(
        "--headless",
        action='store',
        default=False,
        help="Choose mode: true or false "
    )

    parser.addoption(
        "--url",
        default="https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all",
        help="This is request url"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def headless(request):
    return request.config.getoption("--headless")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    mode = request.config.getoption("--headless")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        if mode == "true":
            options = Options()
            options.add_argument("--headless")
            browser = webdriver.Chrome(options=options)
        else:
            options = Options()
            options.add_argument("--start-fullscreen")
            browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        if mode == "true":
            options = Options()
            options.add_argument("--headless")
            browser = webdriver.Firefox(options=options)
        else:
            options = Options()
            options.add_argument("-start-fullscreen")
            browser = webdriver.Firefox(options=options)

    elif browser_name == "IE":
        print("\nstart IE browser for test..")
        browser = webdriver.Ie()

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox or IE")
    yield browser
    print("\nquit browser..")
    browser.quit()
