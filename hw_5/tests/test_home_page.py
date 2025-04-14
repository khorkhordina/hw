import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from hw_5.locators.homepage_loc import HomePageLoc


class TestHomePage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 5)


    def test_cart_button_visible(self):
        cart_btn = self.wait.until(
            EC.visibility_of_element_located(HomePageLoc.cart_btn),
            message="Кнопка корзины не отображается на странице"
        )
        title_text = cart_btn.get_attribute("title")
        assert title_text == "Shopping Cart", f"Некорректное значение атрибута title: {title_text}"


    def test_search_button_visible(self):
        search_btn = self.wait.until(
            EC.visibility_of_element_located(HomePageLoc.search_btn),
            message="Кнопка поиска не отображается на странице"
        )
        assert search_btn.is_displayed()


    def test_logo_visible(self):
        logo = self.wait.until(
            EC.visibility_of_element_located(HomePageLoc.logo),
            message="Логотип не отображается на странице"
        )
        assert logo.get_attribute("alt") == "Your Store"


    def test_nav_menu_visible(self):
        nav_menu = self.wait.until(
            EC.visibility_of_element_located(HomePageLoc.nav_menu),
            message="Меню навигации не отображается на странице"
        )
        assert len(nav_menu.find_elements(By.TAG_NAME, "li")) > 0, "Меню должно содержать пункты"


    def test_currency_switcher(self):
        currency = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//form[contains(@action, 'currency')]//strong")
            ),
            message="Элемент с валютой не отображается"
        )
        assert currency.text == "$", \
            f"По умолчанию должна быть валюта $. Фактически: '{currency.text}'"