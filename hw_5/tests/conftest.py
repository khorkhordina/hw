import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://localhost:80")
    parser.addoption("--headless", action="store_true", default=False)
    parser.addoption("--maximize", action="store_true")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximize = request.config.getoption("--maximize")
    base_url = request.config.getoption("--url")

    if browser_name == "chrome":
        service = ChromiumService()
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        service = FFService()
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Firefox(options=options, service=service)
    elif browser_name == "edge":
        service = EdgeService()
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Edge(service=service,options=options)
    else:
        raise ValueError("Browser name must be either 'chrome', 'firefox' or 'edge'")

    driver.implicitly_wait(3)

    if maximize:
        driver.maximize_window()

    driver.get(base_url)

    driver.url = base_url

    yield driver
    driver.quit()

