import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hw_6.pages.base_page import BasePage
from hw_6.pages.locators.home_page_loc import HomeLocators


class HomePage(BasePage):

    CURRENCY_OPTIONS = {
        'EUR': HomeLocators.CURRENCY_EUR,
        'USD': HomeLocators.CURRENCY_USD,
        'GBP': HomeLocators.CURRENCY_GBP
    }

    def open(self):

        self.browser.get(f"{self.browser.url}")
        self.is_element_visible(HomeLocators.PRICE_ELEMENTS, timeout=10)
        return self

    def select_currency(self, currency_code):

        dropdown = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(HomeLocators.CURRENCY_DROPDOWN)
        )
        ActionChains(self.browser).move_to_element(dropdown).click().perform()
        time.sleep(1)

        if currency_code in self.CURRENCY_OPTIONS:
            currency_element = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(self.CURRENCY_OPTIONS[currency_code])
            )
            ActionChains(self.browser).move_to_element(currency_element).click().perform()
            time.sleep(2)

        return self

    def get_currency_symbol(self):

        symbols = {'€': 'EUR', '$': 'USD', '£': 'GBP'}
        self.wait_for_visible(HomeLocators.PRICE_ELEMENTS)
        price_elements = self.browser.find_elements(*HomeLocators.PRICE_ELEMENTS)[:3]

        for element in price_elements:
            price_text = element.text
            for symbol in symbols:
                if symbol in price_text:
                    return symbol
        return None