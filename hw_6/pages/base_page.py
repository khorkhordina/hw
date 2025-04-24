from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент {locator} не найден"
        )

    def click_element(self, locator, timeout=10):
        element = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {locator} не кликабелен"
        )
        element.click()

    def send_keys(self, locator, text, timeout=10):
        element = WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент {locator} не виден"
        )
        element.clear()
        element.send_keys(text)

    def wait_for_visible(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент {locator} не виден"
        )

    def is_element_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False